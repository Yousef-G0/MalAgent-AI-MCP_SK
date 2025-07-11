import math
from collections import Counter

def run(params):
    content = params.get("content", "")
    if not content:
        return {"error": "Missing 'content' parameter."}

    if isinstance(content, str):
        content = content.encode("utf-8")

    # Calculate Shannon entropy
    length = len(content)
    if length == 0:
        return {"error": "Empty content."}

    counter = Counter(content)
    entropy = -sum((count / length) * math.log2(count / length) for count in counter.values())

    return {
        "entropy_score": round(entropy, 4),
        "length": length
    }
