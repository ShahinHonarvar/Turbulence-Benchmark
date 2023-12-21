
def remove_repeat_chars(s):
    sub_str = s[51:92]
    chars = [char for char in sub_str if sub_str.count(char) > 1]
    no_repeat_str = ''.join([char for char in s if char not in chars])
    return no_repeat_str
