import re
def return_n_smallest_chars(str):
    return sorted(re.findall(r'[A-Z]', str), key=lambda x: ord(x))[:46]
