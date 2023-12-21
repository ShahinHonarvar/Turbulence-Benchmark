import re
def return_n_greatest_chars(s):
    return re.findall(r'(.)\1*', s)[::-1][:45]
