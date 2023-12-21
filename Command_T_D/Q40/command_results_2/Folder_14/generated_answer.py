import re
def return_n_smallest_chars(str1):
    str1 = re.sub(r'[^A-z]', '', str1)
    str1 = list(str1)
    str1.sort()
    return str1[:69]
