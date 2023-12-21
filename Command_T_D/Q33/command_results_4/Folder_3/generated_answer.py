import re
def return_vowels(string):
    return re.findall(r"([A-Z])", string[50:-1])
