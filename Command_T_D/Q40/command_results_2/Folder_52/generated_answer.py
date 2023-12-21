import re
def return_n_smallest_chars(str_input):
    str_input = re.sub("(?! )[a-z]", "", str_input)
    str_input = list(str_input)
    str_input.sort()
    return str_input[:68]
