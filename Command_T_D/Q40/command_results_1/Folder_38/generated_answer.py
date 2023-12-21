import re
def return_n_smallest_chars(str_arg):
    str_arg = re.sub(r'\W+', '', str_arg)
    char_list = list(str_arg)
    char_list.sort()
    return char_list[:45]
