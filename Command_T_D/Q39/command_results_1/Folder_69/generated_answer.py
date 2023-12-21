import re
def return_n_greatest_chars(s):
    m = re.fullmatch(r'<\d+>(\D+)<', s)
    if not m:
        raise ValueError("Text specification is not a substring of given string")
    n = int(m.group(1))
    return sorted(set(m.group(2)), key=lambda x: ord(x))[:n]
