# PDF Tools MCP Server

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

A FastMCP server for creating, reading, and updating PDF files programmatically. Built with [FastMCP](https://github.com/jlowin/fastmcp), this server provides a simple HTTP API for PDF manipulation tasks.

## 🌟 Features

### 📝 Create PDFs
Create new PDF documents with text content:
```python
create_pdf(
    output_path="document.pdf",
    text="Hello, World!\nThis is a new PDF.",
    title="My Document"
)
```

### 📖 Read PDFs
Extract text content and metadata from existing PDFs:
```python
read_pdf(file_path="document.pdf")
# Returns: {num_pages, metadata, pages: [{page, text}]}
```

### ✏️ Update PDFs
Add new text to existing PDF pages:
```python
update_pdf(
    input_path="original.pdf",
    output_path="updated.pdf",
    page_number=1,
    new_text="Additional content"
)
```

### 🔗 Merge PDFs
Combine multiple PDF files into one:
```python
merge_pdfs(
    input_paths=["file1.pdf", "file2.pdf", "file3.pdf"],
    output_path="merged.pdf"
)
```

### ✂️ Extract Pages
Extract specific pages from a PDF:
```python
extract_pages(
    input_path="document.pdf",
    output_path="extracted.pdf",
    start_page=1,
    end_page=5
)
```

## 📋 Prerequisites

- Python 3.8 or higher
- pip package manager

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/mcp-server-setup.git
cd mcp-server-setup
```

### 2. Install Dependencies

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run the Server

```bash
python main.py
```

The server will start on `http://localhost:8000`

## 💻 Available Tools

### `create_pdf`
Create a new PDF file with text content.

**Parameters:**
- `output_path` (str): Path where the PDF will be saved
- `text` (str): Text content to add to the PDF
- `title` (str, optional): Title for the PDF document

**Returns:** Success message with file path

**Example:**
```python
create_pdf(
    output_path="/tmp/my_document.pdf",
    text="Chapter 1\n\nThis is the beginning of my story...",
    title="My Story"
)
```

---

### `read_pdf`
Read and extract text content from a PDF file.

**Parameters:**
- `file_path` (str): Path to the PDF file to read

**Returns:** Dictionary containing:
- `num_pages`: Total number of pages
- `metadata`: PDF metadata (title, author, creator)
- `pages`: Array of page objects with page number and extracted text

**Example:**
```python
result = read_pdf(file_path="/tmp/document.pdf")
print(f"Pages: {result['num_pages']}")
for page in result['pages']:
    print(f"Page {page['page']}: {page['text'][:100]}...")
```

---

### `update_pdf`
Update a PDF by adding new text to a specific page.

**Parameters:**
- `input_path` (str): Path to the input PDF file
- `output_path` (str): Path where the updated PDF will be saved
- `page_number` (int): Page number to update (1-indexed)
- `new_text` (str): New text to add to the page

**Returns:** Success message with output file path

**Example:**
```python
update_pdf(
    input_path="/tmp/original.pdf",
    output_path="/tmp/updated.pdf",
    page_number=1,
    new_text="Updated on 2025-12-05"
)
```

---

### `merge_pdfs`
Merge multiple PDF files into a single PDF.

**Parameters:**
- `input_paths` (List[str]): List of paths to PDF files to merge
- `output_path` (str): Path where the merged PDF will be saved

**Returns:** Success message with output file path

**Example:**
```python
merge_pdfs(
    input_paths=[
        "/tmp/chapter1.pdf",
        "/tmp/chapter2.pdf",
        "/tmp/chapter3.pdf"
    ],
    output_path="/tmp/complete_book.pdf"
)
```

---

### `extract_pages`
Extract specific pages from a PDF file.

**Parameters:**
- `input_path` (str): Path to the input PDF file
- `output_path` (str): Path where the extracted pages will be saved
- `start_page` (int): Starting page number (1-indexed, inclusive)
- `end_page` (int): Ending page number (1-indexed, inclusive)

**Returns:** Success message with output file path

**Example:**
```python
extract_pages(
    input_path="/tmp/full_document.pdf",
    output_path="/tmp/summary.pdf",
    start_page=1,
    end_page=3
)
```

## 📁 Project Structure

```
mcp-server-setup/
├── main.py               # Main FastMCP server with PDF tools
├── requirements.txt      # Python dependencies
├── README.md            # This file
└── .gitignore
```

## 🐛 Troubleshooting

### "File not found" errors
- Ensure you're using absolute paths or correct relative paths
- Verify the file exists before attempting to read/update
- Check file permissions

### "Invalid page range" errors
- Page numbers are 1-indexed (first page is 1, not 0)
- Ensure start_page <= end_page
- Verify page numbers don't exceed the PDF's total pages

### PDF creation issues
- Ensure the output directory exists
- Check write permissions for the output path
- For long text, consider pagination (current implementation is basic)

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Ways to Contribute

- 🐛 **Report bugs** - Open an issue with details
- 💡 **Suggest features** - Share your ideas for improvements
- 📝 **Improve documentation** - Help make the docs clearer
- 🔧 **Submit PRs** - Fix bugs or add features

### Getting Started

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test thoroughly
5. Commit with clear messages
6. Push and open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

### Code of Conduct

Please be respectful and constructive in all interactions. We're here to build something great together!

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [FastMCP](https://github.com/jlowin/fastmcp) - Excellent MCP framework
- [pypdf](https://pypdf.readthedocs.io/) - Powerful PDF manipulation library
- [ReportLab](https://www.reportlab.com/) - PDF generation toolkit
- All our [contributors](https://github.com/yourusername/mcp-server-setup/graphs/contributors)

## 🔗 Resources

- [pypdf Documentation](https://pypdf.readthedocs.io/)
- [ReportLab Documentation](https://www.reportlab.com/docs/reportlab-userguide.pdf)
- [FastMCP Documentation](https://github.com/jlowin/fastmcp)
- [MCP Protocol Specification](https://modelcontextprotocol.io/)

## ⭐ Star History

If you find this project useful, please consider giving it a star! It helps others discover the project.

---

Made with ❤️ for the MCP community
