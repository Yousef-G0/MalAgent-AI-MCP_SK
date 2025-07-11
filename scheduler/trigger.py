import subprocess
import datetime

def log(msg):
    print(f"[{datetime.datetime.utcnow().isoformat()}] {msg}")

def run_agent():
    log("Starting MalAgent...")
    subprocess.run(["python3", "sk_agent/agent.py"])
    log("MalAgent finished.")

if __name__ == "__main__":
    run_agent()
