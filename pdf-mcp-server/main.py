"""
PDF Tools MCP Server

A FastMCP server for creating, reading, and updating PDF files.
"""

from fastmcp import FastMCP
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io
import os

mcp = FastMCP("PDF Tools MCP Server")


@mcp.tool
def create_pdf(output_path: str, text: str, title: str = "Document") -> str:
    """
    Create a new PDF file with the given text content.
    
    Args:
        output_path: Path where the PDF will be saved
        text: Text content to add to the PDF
        title: Optional title for the PDF document
        
    Returns:
        Success message with file path
    """
    # Create a PDF using reportlab
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    
    # Set title
    can.setTitle(title)
    
    # Add title to page
    can.setFont("Helvetica-Bold", 16)
    can.drawString(50, 750, title)
    
    # Add text content
    can.setFont("Helvetica", 12)
    text_object = can.beginText(50, 720)
    text_object.setFont("Helvetica", 12)
    
    # Split text into lines and add to PDF
    lines = text.split('\n')
    for line in lines:
        text_object.textLine(line)
    
    can.drawText(text_object)
    can.save()
    
    # Write to file
    packet.seek(0)
    with open(output_path, 'wb') as f:
        f.write(packet.getvalue())
    
    return f"PDF created successfully at: {output_path}"


@mcp.tool
def read_pdf(file_path: str) -> dict:
    """
    Read and extract text content from a PDF file.
    
    Args:
        file_path: Path to the PDF file to read
        
    Returns:
        Dictionary containing text content and metadata
    """
    if not os.path.exists(file_path):
        return {"error": f"File not found: {file_path}"}
    
    reader = PdfReader(file_path)
    
    # Extract text from all pages
    text_content = []
    for i, page in enumerate(reader.pages):
        text_content.append({
            "page": i + 1,
            "text": page.extract_text()
        })
    
    # Get metadata
    metadata = reader.metadata
    
    return {
        "num_pages": len(reader.pages),
        "metadata": {
            "title": metadata.get("/Title", "N/A") if metadata else "N/A",
            "author": metadata.get("/Author", "N/A") if metadata else "N/A",
            "creator": metadata.get("/Creator", "N/A") if metadata else "N/A",
        },
        "pages": text_content
    }


@mcp.tool
def update_pdf(input_path: str, output_path: str, page_number: int, new_text: str) -> str:
    """
    Update a PDF by adding new text to a specific page.
    
    Args:
        input_path: Path to the input PDF file
        output_path: Path where the updated PDF will be saved
        page_number: Page number to update (1-indexed)
        new_text: New text to add to the page
        
    Returns:
        Success message with output file path
    """
    if not os.path.exists(input_path):
        return f"Error: Input file not found: {input_path}"
    
    # Read existing PDF
    reader = PdfReader(input_path)
    writer = PdfWriter()
    
    # Create new content for the specified page
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    can.setFont("Helvetica", 10)
    
    # Add new text at bottom of page
    can.drawString(50, 50, new_text)
    can.save()
    
    # Move to the beginning of the BytesIO buffer
    packet.seek(0)
    new_pdf = PdfReader(packet)
    
    # Add all pages, merging the new content with the specified page
    for i, page in enumerate(reader.pages):
        if i == page_number - 1:  # Convert to 0-indexed
            page.merge_page(new_pdf.pages[0])
        writer.add_page(page)
    
    # Write to output file
    with open(output_path, 'wb') as output_file:
        writer.write(output_file)
    
    return f"PDF updated successfully. Saved to: {output_path}"


@mcp.tool
def merge_pdfs(input_paths: list[str], output_path: str) -> str:
    """
    Merge multiple PDF files into a single PDF.
    
    Args:
        input_paths: List of paths to PDF files to merge
        output_path: Path where the merged PDF will be saved
        
    Returns:
        Success message with output file path
    """
    writer = PdfWriter()
    
    for path in input_paths:
        if not os.path.exists(path):
            return f"Error: File not found: {path}"
        
        reader = PdfReader(path)
        for page in reader.pages:
            writer.add_page(page)
    
    with open(output_path, 'wb') as output_file:
        writer.write(output_file)
    
    return f"PDFs merged successfully. Saved to: {output_path}"


@mcp.tool
def extract_pages(input_path: str, output_path: str, start_page: int, end_page: int) -> str:
    """
    Extract specific pages from a PDF file.
    
    Args:
        input_path: Path to the input PDF file
        output_path: Path where the extracted pages will be saved
        start_page: Starting page number (1-indexed, inclusive)
        end_page: Ending page number (1-indexed, inclusive)
        
    Returns:
        Success message with output file path
    """
    if not os.path.exists(input_path):
        return f"Error: Input file not found: {input_path}"
    
    reader = PdfReader(input_path)
    writer = PdfWriter()
    
    # Validate page numbers
    if start_page < 1 or end_page > len(reader.pages):
        return f"Error: Invalid page range. PDF has {len(reader.pages)} pages."
    
    # Extract pages (convert to 0-indexed)
    for i in range(start_page - 1, end_page):
        writer.add_page(reader.pages[i])
    
    with open(output_path, 'wb') as output_file:
        writer.write(output_file)
    
    return f"Pages {start_page}-{end_page} extracted successfully. Saved to: {output_path}"


if __name__ == "__main__":
    print("🚀 Starting PDF Tools MCP Server...")
    print("📄 Available tools:")
    print("  - create_pdf: Create a new PDF with text content")
    print("  - read_pdf: Extract text and metadata from a PDF")
    print("  - update_pdf: Add text to an existing PDF page")
    print("  - merge_pdfs: Merge multiple PDFs into one")
    print("  - extract_pages: Extract specific pages from a PDF")
    
    mcp.run()
