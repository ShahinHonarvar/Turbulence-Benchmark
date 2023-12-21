import re
def return_n_greatest_chars(str1):
    str1 = re.sub(r'[^A-z0-9]+', '', str1)
    return sorted(str1, key=str.lower)[:7]
