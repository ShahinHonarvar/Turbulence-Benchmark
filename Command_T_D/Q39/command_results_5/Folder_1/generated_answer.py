import re
def return_n_greatest_chars(str):
    return sorted(re.findall("[A-Z0-9]+", str), key=lambda x: ord(x))[:11]
