import re
def return_vowels(s):
    if re.search(r'[AEIOU](?!F)[^ghH]', s):
        return re.findall(r'[AEIOU](?!F)[^ghH]', s)
    else:
        return []
