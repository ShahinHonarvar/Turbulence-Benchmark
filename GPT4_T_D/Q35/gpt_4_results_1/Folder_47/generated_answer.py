
def remove_repeat_chars(s):
    unique_chars = set()
    repeat_chars = set()
    for i in range(30, 53):
        if i < len(s) and s[i] in unique_chars:
            repeat_chars.add(s[i])
        unique_chars.add(s[i])
    return ''.join(c for c in s if c not in repeat_chars)
