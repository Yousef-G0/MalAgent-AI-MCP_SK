import requests
import json
from planner import plan_malware_task

MCP_SERVER = "http://localhost:8000"

def list_tools():
    response = requests.get(f"{MCP_SERVER}/tools")
    return {tool['name']: tool for tool in response.json()}

def call_tool(name, parameters):
    response = requests.post(f"{MCP_SERVER}/tools/{name}", json={"parameters": parameters})
    return response.json()

def main():
    print("🤖 Starting MalAgent AI")
    tools = list_tools()

    # Example: Generate polymorphic dropper
    task = "Generate a polymorphic dropper that evades basic static analysis."
    plan = plan_malware_task(task)
    print("🧠 Plan:", plan)

    # Step 1: Generate Payload
    payload = plan["generate"]

    # Step 2: Obfuscate
    obf_result = call_tool("obfuscate_code", {"code": payload})
    obfuscated_code = obf_result.get("obfuscated_code", "")

    # Step 3: YARA Scan
    yara_result = call_tool("yara_scan", {"content": obfuscated_code})

    # Step 4: Entropy Check
    entropy_result = call_tool("entropy_check", {"content": obfuscated_code})

    # Step 5: Generate Report
    report = f"""# Malware Analysis Report

**Task**: {task}

## Obfuscated Payload:
```python
{obfuscated_code}
```

## YARA Matches:
{yara_result.get('matches')}

## Entropy Score:
{entropy_result.get('entropy_score')}
"""

    # Step 6: Upload Report
    upload_result = call_tool("report_uploader", {
        "report": report,
        "name": "polymorphic_dropper"
    })

    print("✅ Report saved:", upload_result.get("saved_path"))

if __name__ == "__main__":
    main()
