def plan_malware_task(task_description):
    """
    Simulates a planning step by returning a hardcoded payload
    for the given malware task description.
    """
    print(f"📋 Planning task: {task_description}")

    return {
        "generate": """
# Sample Polymorphic Dropper
import base64
import time
import os

def drop():
    b = base64.b64decode('aGVsbG8gd29ybGQ=')
    with open('/tmp/drop.bin', 'wb') as f:
        f.write(b)
    os.system('chmod +x /tmp/drop.bin')
    time.sleep(3)
    os.system('/tmp/drop.bin')

drop()
"""
    }
