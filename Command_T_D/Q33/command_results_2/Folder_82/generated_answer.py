import re
def return_vowels(s):
    try:
        return re.findall(r'[aeiou]', s[86:-1])
    except:
        return []
