from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List, Dict
import uvicorn
import importlib
import os
import json

app = FastAPI(title="MalAgent MCP Server")

# Define MCP-compatible structure
class MCPToolDescription(BaseModel):
    name: str
    description: str
    parameters: Dict[str, str]

# Registry to simulate tool discovery
TOOLS = {
    "obfuscate_code": {
        "description": "Obfuscates a given Python payload using simple transformations.",
        "parameters": {"code": "Python code to obfuscate"}
    },
    "yara_scan": {
        "description": "Scans the given file content using YARA rules.",
        "parameters": {"content": "File content to scan"}
    },
    "entropy_check": {
        "description": "Returns entropy score of a given binary blob.",
        "parameters": {"content": "Binary content"}
    },
    "report_uploader": {
    "description": "Uploads or stores a markdown report locally.",
    "parameters": {
        "report": "Markdown report content",
        "name": "Base name of the report"
    }
}

}

@app.get("/tools", response_model=List[MCPToolDescription])
def list_tools():
    return [MCPToolDescription(name=name, **info) for name, info in TOOLS.items()]

class ToolRequest(BaseModel):
    parameters: Dict[str, str]

@app.post("/tools/{tool_name}")
def invoke_tool(tool_name: str, request: ToolRequest):
    try:
        tool_module = importlib.import_module(f"tools.{tool_name}_tool")
        return tool_module.run(request.parameters)
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
