# 🦠 MalAgent AI

**MalAgent AI** is an automated malware analysis and generation system using [Semantic Kernel]-style planning and [Model Context Protocol (MCP)] for dynamic tool integration.

It allows you to:
- Generate polymorphic malware samples
- Obfuscate payloads
- Analyze using YARA-like rules and entropy
- Generate and store threat reports

Everything is modular and written in **Python** for compatibility with **Kali Linux**.

---

## 🧩 Project Structure

```bash
malagent-ai/
├── mcp_server/            # FastAPI server exposing tools
│   ├── tools/             # MCP tools (each file = one tool)
│   │   ├── obfuscate_code_tool.py
│   │   ├── yara_scan_tool.py
│   │   ├── entropy_check_tool.py
│   │   └── report_uploader_tool.py
│   └── mcp_server.py
│
├── sk_agent/              # Semantic agent (reasoner)
│   ├── agent.py
│   ├── planner.py
│   ├── __init__.py
│   └── prompts/
│       ├── generate_payload.txt
│       └── generate_report.txt
│
├── memory/
│   └── db.json            # Stores execution logs
│
├── scheduler/
│   └── trigger.py         # CLI/cron trigger
│
├── .env                   # Environment config (MCP_SERVER, etc.)
├── requirements.txt       # Python dependencies
└── README.md

```

## 🚀 Features

- 🔄 Dynamic tool discovery via MCP
- 🦠 Payload generation + obfuscation
- 🔍 Static analysis (YARA + entropy scan)
- 📄 Report generation and local storage
- ⏱️ Scheduler support for automated runs

---


## ✅ Setup Instructions

```bash
# 1. Clone the project and navigate into it
cd malagent

# 2. Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the MCP server (in one terminal)
cd mcp_server
python3 mcp_server.py

# 5. Run the agent (in another terminal)
cd sk_agent
python3 agent.py
```

---

## 🧪 How to Trigger from CLI

```bash
python3 scheduler/trigger.py
```

---

## 🧠 Prompt Logic
- Payload and report generation are powered by static prompt templates.
- These live in `sk_agent/prompts/`.
- You can manually modify them for different tasks.

---

## 🔐 Environment Config (.env)

Optional file to define things like:
```
REPORT_DIR=uploaded_reports
MCP_SERVER=http://localhost:8000
```

---

##  Optional: Claude Sonnet  OR OpenAI Integration (Future Use)

Create a folder:
```
optional_models/
├── claude_sonnet_client.py   # Use Anthropic API key here
```

```
optional_models/
├── openai_gpt4.5_client.py   # Use OpenAI API key here
```

Use this folder to house Claude-related or OpenAI logic later if you decide to extend the planner or generation via Sonnet 4 or gpt4.5.

---

## License / Legal
 For red-team lab use only. Do not use it for malicious purposes.

---

Enjoy hacking the stack, responsibly. 
