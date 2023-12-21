
def remove_repeat_chars(s):
    repeated_chars = [ch for ch in s[57:90] if s[57:90].count(ch) > 1]
    result = ''.join([ch for ch in s if ch not in repeated_chars])
    return result
