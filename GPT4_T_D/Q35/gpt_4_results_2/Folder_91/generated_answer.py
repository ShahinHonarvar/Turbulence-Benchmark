
def remove_repeat_chars(s):
    s_list = list(s)
    repeat_chars = [ch for ch in s[1:6] if s[1:6].count(ch) > 1]
    
    for ch in repeat_chars:
        while ch in s_list:
            s_list.remove(ch)
    return ''.join(s_list)
