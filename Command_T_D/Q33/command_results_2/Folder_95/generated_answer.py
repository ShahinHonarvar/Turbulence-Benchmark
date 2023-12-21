import re
def return_vowels(string):
    return re.findall("[aeiou]", string)[2:-2]
