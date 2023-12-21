
def filter_chars(s):
    chars_to_remove = []
    for i in range(35, min(99, len(s))):
        if 'A' <= s[i] <= 'b':
            chars_to_remove.append(s[i])
            
    return ''.join(c for c in s if c not in chars_to_remove)
