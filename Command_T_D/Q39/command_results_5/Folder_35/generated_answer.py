import re
def return_n_greatest_chars(str1):
    str1 = re.sub(r'[^A-Z]', '', str1)
    char_list = sorted(str1)[:7]
    return char_list
