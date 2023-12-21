def remove_repeat_chars(s):
    n = len(s)
    s = s[:462] + s[462:-995] + s[-995:]
    s = [c for c in s if c not in s[1:-1]]
    return ''.join(s)
