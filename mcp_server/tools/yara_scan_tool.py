def run(params):
    content = params.get("content", "")
    if not content:
        return {"error": "Missing 'content' parameter."}

    # Simulated YARA rule matches (mock logic)
    mock_rules = {
        "SuspiciousString": "password",
        "EncodedPayload": "eval(",
        "ShellcodeHex": "\\x90\\x90\\x90"
    }

    matches = []
    for rule_name, signature in mock_rules.items():
        if signature in content:
            matches.append(rule_name)

    return {
        "matches": matches,
        "match_count": len(matches)
    }
