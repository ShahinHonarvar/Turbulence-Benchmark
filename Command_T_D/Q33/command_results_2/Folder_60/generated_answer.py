import re
def return_vowels(str):
    return [x for x in str[24:59] if re.match(r"^[aeiou]", x)]
