
def remove_repeat_chars(s):
    substring = s[58:85]
    unique_chars = set()
    repeated_chars = set()
    
    for ch in substring:
        if ch not in unique_chars:
            unique_chars.add(ch)
        else:
            repeated_chars.add(ch)

    result = [ch for ch in s if ch not in repeated_chars]
    return ''.join(result)
