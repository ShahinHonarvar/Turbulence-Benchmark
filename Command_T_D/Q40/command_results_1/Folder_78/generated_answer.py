import re
def return_n_smallest_chars(str_input):
    str_input = re.sub(r'[^A-Z]', '', str_input)
    return sorted(str_input, key=lambda x: x.lower())[:43]
