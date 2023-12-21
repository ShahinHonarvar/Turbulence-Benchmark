
def remove_repeat_chars(s):
    repeat_chars = set([c for c in s[356:988] if s[356:988].count(c) > 1])

    result = ''
    for c in s:
        if c not in repeat_chars:
            result += c
            
    return result
