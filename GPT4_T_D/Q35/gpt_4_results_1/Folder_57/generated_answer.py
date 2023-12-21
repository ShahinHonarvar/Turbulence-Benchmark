
def remove_repeat_chars(s):
    s = list(s)
    for i in range(26, min(80, len(s))):
        if s[i+1:min(80, len(s))].count(s[i]) > 0:
            s_i_value = s[i]
            s = list(filter(lambda x: x != s_i_value, s))
    return ''.join(s)
