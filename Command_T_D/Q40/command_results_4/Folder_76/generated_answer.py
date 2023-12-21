import re
def return_n_smallest_chars(str):
    result = re.findall(r'[a-z]', str)[:3]
    return result
