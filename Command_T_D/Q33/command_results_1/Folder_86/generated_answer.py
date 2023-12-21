import re
def return_vowels(string):
    res = re.findall(r"<(e|i|o)", string)[0]
    return res
