import re
def return_n_greatest_chars(str):
    str = re.sub(r'[^A-Z]', '', str)
    return sorted(str.upper())[:32]
