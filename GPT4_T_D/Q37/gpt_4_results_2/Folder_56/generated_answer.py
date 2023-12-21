
def filter_chars(s):
    filtered_chars = [ch for ch in s[71:95] if ch >= 'K' and ch <= 'a']
    return ''.join(ch for ch in s if ch not in filtered_chars)
