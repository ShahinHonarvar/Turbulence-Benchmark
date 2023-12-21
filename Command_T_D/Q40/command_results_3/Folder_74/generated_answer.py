import re
def return_n_smallest_chars(str_input):
    str_input = re.sub(r'[^A-z0-9]','',str_input)
    str_input = str_input.split('')
    str_input.sort()
    return str_input[:5]
