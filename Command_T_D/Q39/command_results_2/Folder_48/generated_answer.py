import re
def return_n_greatest_chars(s):
    return re.findall(r'\w+', s)[12:][::-1]
