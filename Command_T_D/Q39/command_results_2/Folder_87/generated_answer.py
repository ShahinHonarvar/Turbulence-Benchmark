import re
def return_n_greatest_chars(str):
    str = re.sub(r'\s+', '', str)
    return sorted(str, key=lambda x: ord(x))[:24]
