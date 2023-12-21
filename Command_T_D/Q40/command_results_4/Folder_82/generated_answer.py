import re
def return_n_smallest_chars(s):
    result = re.findall(r'[A-z]', s)[:60]
    result.sort()
    return result
