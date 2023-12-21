import re
def return_vowels(str):
    return re.findall("[aeiou]", str[13:-1])
