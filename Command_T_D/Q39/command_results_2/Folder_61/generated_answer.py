import re
def return_n_greatest_chars(str_input):
    str_input = re.sub(r'[^A-z0-9]', '', str_input)
    char_list = list(str_input)
    char_list.sort(key=lambda x: ord(x))
    return char_list[:66]
