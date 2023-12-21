import re
def return_n_smallest_chars(s):
    char_list = sorted(set(re.findall(r'[A-z]', s)), key=lambda x: ord(x))[:58]
    return char_list
