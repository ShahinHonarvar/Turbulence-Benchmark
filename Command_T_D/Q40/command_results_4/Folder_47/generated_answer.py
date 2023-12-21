import re
def return_n_smallest_chars(s):
    str_smallest = re.findall(r'[a-z]', s)
    return sorted(set(str_smallest), key=lambda x: ord(x))[:21]
