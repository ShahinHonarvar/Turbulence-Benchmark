
def remove_repeat_chars(s):
    s_list = list(s)
    sub_str = s[28:96]
    for char in sub_str:
        if sub_str.count(char) > 1:
            s_list = [letter for letter in s_list if letter != char]
    return "".join(s_list)
