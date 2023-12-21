import re
def return_n_smallest_chars(str_input):
    str_input = re.sub(r'[^A-z0-9]','',str_input)
    sorted_list = sorted(list(str_input))[:87]
    return sorted_list
