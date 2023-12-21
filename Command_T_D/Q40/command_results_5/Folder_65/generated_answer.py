import re
def return_n_smallest_chars(s):
    ascii_re = re.compile("[A-Z]+")
    return sorted(list(set(ascii_re.findall(s))), key=lambda c: ord(c))[:27]
