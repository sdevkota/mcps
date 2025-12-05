#!/usr/bin/env python3
"""Test script to verify the MCP server works correctly."""

import subprocess
import json
import sys

def test_mcp_server():
    """Test the MCP server by sending a list_tools request."""
    
    # Start the server process
    process = subprocess.Popen(
        ["python", "main.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        cwd="/Users/sudeep/apps/mcps/weather-mcp"
    )
    
    # Send initialize request
    initialize_request = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {
                "name": "test-client",
                "version": "1.0.0"
            }
        }
    }
    
    try:
        # Send the request
        process.stdin.write(json.dumps(initialize_request) + "\n")
        process.stdin.flush()
        
        # Read the response
        response_line = process.stdout.readline()
        if response_line:
            response = json.loads(response_line)
            print("✅ Server initialized successfully!")
            print(f"Response: {json.dumps(response, indent=2)}")
            
            # Send list_tools request
            list_tools_request = {
                "jsonrpc": "2.0",
                "id": 2,
                "method": "tools/list"
            }
            
            process.stdin.write(json.dumps(list_tools_request) + "\n")
            process.stdin.flush()
            
            tools_response = process.stdout.readline()
            if tools_response:
                tools = json.loads(tools_response)
                print("\n✅ Tools listed successfully!")
                print(f"Available tools: {json.dumps(tools, indent=2)}")
                
                if "result" in tools and "tools" in tools["result"]:
                    tool_names = [t["name"] for t in tools["result"]["tools"]]
                    if "get_weather" in tool_names:
                        print("\n✅ get_weather tool found!")
                        return True
                    else:
                        print("\n❌ get_weather tool not found in tools list")
                        return False
        else:
            print("❌ No response from server")
            return False
            
    except Exception as e:
        print(f"❌ Error testing server: {e}")
        return False
    finally:
        process.terminate()
        process.wait()

if __name__ == "__main__":
    success = test_mcp_server()
    sys.exit(0 if success else 1)
