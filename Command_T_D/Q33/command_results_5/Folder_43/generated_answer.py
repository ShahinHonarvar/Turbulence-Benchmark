import re
def return_vowels(s):
    res = re.findall(r'[aeiou]{22,82}', s)
    if not res:
        return []
    return res[1:]
