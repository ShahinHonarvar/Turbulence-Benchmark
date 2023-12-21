
def filter_chars(s: str) -> str:
    return ''.join(c for i, c in enumerate(s) if i < 41 or i > 64 or not 'K' <= c <= ']')
