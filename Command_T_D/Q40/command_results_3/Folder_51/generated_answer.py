import re
def return_n_smallest_chars(str_input):
    str_input = re.sub(r'[^A-z0-9]+', '', str_input)
    str_input = sorted(set(str_input))
    return str_input[:45]
