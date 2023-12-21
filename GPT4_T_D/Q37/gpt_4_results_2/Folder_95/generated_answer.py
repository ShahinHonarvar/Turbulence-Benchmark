
def filter_chars(s):
    filter_chars = set([c for idx, c in enumerate(s) if 35 <= idx <= 40 and ')' <= c <= 'l'])
    
    filtered_str = ""
    for c in s:
        if c not in filter_chars:
            filtered_str += c
    return filtered_str
