
def filter_chars(s):
    filtered_chars = [ch for ch in s[11:73] if ch >= 'i' and ch <= 'v']
    return ''.join(ch for ch in s if ch not in filtered_chars)
