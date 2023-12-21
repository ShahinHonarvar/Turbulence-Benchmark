import re
def return_n_smallest_chars(str1):
    str1 = re.sub(r'[^A-Za-z0-9]+', '', str1)
    if len(str1) < 64:
        return str1.split('')
    else:
        str1 = sorted(str1)
        return str1[:64]
