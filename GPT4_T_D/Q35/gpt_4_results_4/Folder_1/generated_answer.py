
def remove_repeat_chars(s):
    s_list = list(s)
    repeat_chars = set([char for char in s[18:88] if s[18:88].count(char) > 1])
    s_list = [char for char in s_list if char not in repeat_chars]
    return ''.join(s_list)
