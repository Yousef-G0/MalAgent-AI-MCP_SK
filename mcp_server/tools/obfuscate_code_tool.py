def run(params):
    code = params.get("code", "")
    if not code:
        return {"error": "Missing 'code' parameter."}

    import re
    import random
    import string

    # Find all variable-like words (very basic heuristic)
    identifiers = set(re.findall(r"\\b[a-zA-Z_][a-zA-Z0-9_]*\\b", code))
    reserved = {
        "def", "return", "if", "else", "for", "while", "import", "from", "in", "print",
        "and", "or", "not", "True", "False", "None", "class", "with", "as", "try", "except"
    }
    variables = [v for v in identifiers if v not in reserved and not v.startswith("__")]

    obfuscated = {}
    for var in variables:
        obfuscated[var] = "_" + ''.join(random.choices(string.ascii_letters, k=8))

    for old, new in obfuscated.items():
        code = re.sub(rf"\\b{old}\\b", new, code)

    return {"obfuscated_code": code}
