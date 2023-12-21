
def remove_repeat_chars(s):
    s_list = list(s)
    substring = s[41:200]
    repeated_chars = [c for c in substring if substring.count(c) > 1]
    for c in repeated_chars:
        while c in s_list:
            s_list.remove(c)
    return ''.join(s_list)
