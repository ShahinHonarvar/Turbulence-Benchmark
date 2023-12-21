
def remove_repeat_chars(s):
    s_chars = list(s)
    for char in s[104:802]:
        if s[104:802].count(char) > 1:
            s_chars = [c for c in s_chars if c != char]
    return ''.join(s_chars)
