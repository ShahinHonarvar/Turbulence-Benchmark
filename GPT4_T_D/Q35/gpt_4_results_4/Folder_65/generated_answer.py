
def remove_repeat_chars(s):
    substring = s[52:76]
    unique_chars = set(substring)
    for char in unique_chars:
        if substring.count(char) > 1:
            s = s.replace(char, "")
    return s
