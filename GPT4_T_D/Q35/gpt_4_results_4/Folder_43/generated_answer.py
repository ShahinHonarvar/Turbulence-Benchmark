
def remove_repeat_chars(s):
    unique_chars = set(s[11:28])
    repeated_chars = {ch for ch in unique_chars if s[11:28].count(ch) > 1}
    return ''.join(ch for ch in s if ch not in repeated_chars)
