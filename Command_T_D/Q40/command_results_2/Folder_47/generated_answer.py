import re
def return_n_smallest_chars(str):
    str = re.sub(r'[^A-z]', '', str)
    str = sorted(str)
    return str[:21]
