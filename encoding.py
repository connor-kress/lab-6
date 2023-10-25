def encode(string: str) -> str:
    return ''.join(str((int(c)+3) % 10) for c in string)

def decode(string: str) -> str:
    return ''.join(str((int(c)-3) % 10) for c in string)
