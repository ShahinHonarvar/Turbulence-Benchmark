
def remove_repeat_chars(s):
    s_list = list(s)
    s_set = set(s_list[71:98])
    for char in s_set:
        if s_list[71:98].count(char) > 1:
            s_list = [c for c in s_list if c != char]
            
    return ''.join(s_list)
