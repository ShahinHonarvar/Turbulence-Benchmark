import re
def return_n_greatest_chars(s):
    ascii_re = re.compile("|".join(str(c) for c in range(ord("A"), ord("z") + 1)))
    return sorted(set(ascii_re.findall(s)), key=lambda x: ord(x))[:23]
