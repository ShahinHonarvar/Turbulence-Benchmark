import re
def return_n_greatest_chars(str1):
    str1 = re.sub(r'[^A-z]', '', str1)
    return str1[::-1][:21]
