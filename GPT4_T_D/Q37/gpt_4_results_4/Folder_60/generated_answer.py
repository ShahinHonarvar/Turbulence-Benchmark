
def filter_chars(s):
    selected_chars = set([ch for ch in s[12:78] if ':' <= ch <= 'L'])
    return "".join([ch for ch in s if ch not in selected_chars])
