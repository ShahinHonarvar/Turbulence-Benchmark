import re
def return_n_greatest_chars(s):
    ascii_re = re.compile("|".join(map(str, range(ord("A") - 1, ord("z") + 1))))
    return sorted(re.findall(ascii_re, s), key=lambda c: ord(c))[:23]
