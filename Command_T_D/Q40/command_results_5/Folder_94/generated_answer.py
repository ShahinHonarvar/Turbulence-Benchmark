import re
def return_n_smallest_chars(s):
    s = re.findall("[A-Z]", s)
    s.sort(key=lambda x: ord(x))
    return s[:87]
