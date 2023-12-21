import re
def return_n_greatest_chars(str):
    return sorted(re.findall(r'[A-Z]', str), key=str.index)[:57]
