
def remove_repeat_chars(s):
    repeated_chars = [ch for ch in s[2:4] if s[2:4].count(ch) > 1]
    result = ""
    for ch in s:
        if ch not in repeated_chars:
            result += ch
    return result
