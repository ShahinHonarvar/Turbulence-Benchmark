
def remove_repeat_chars(s):
    s_list = list(s)
    repeat_char = [ch for ch in s[44:70] if s[44:70].count(ch) > 1]  
    s_no_repeat = ''.join([ch for ch in s_list if ch not in repeat_char])
    return s_no_repeat
