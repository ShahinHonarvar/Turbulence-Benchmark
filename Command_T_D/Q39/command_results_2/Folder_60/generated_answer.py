import re
def return_n_greatest_chars(str1):
    str1 = re.sub(r'[^A-Z0-9]+', '', str1)
    return sorted(str1[::-1])[:28]
