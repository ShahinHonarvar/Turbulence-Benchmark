
def filter_chars(string):
    result = list(string)
    filtered_chars = [ch for ch in result[10:15] if ch > 't' and ch < 'v']
    for ch in filtered_chars:
        result = [c for c in result if c != ch]
    return ''.join(result)
