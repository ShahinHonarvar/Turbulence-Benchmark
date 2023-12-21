
def remove_repeat_chars(s):
    s_list = list(s)
    substring = s[91:97]
    for char in substring:
        if substring.count(char) > 1:
            s_list = [c for c in s_list if c != char]
    return ''.join(s_list)
