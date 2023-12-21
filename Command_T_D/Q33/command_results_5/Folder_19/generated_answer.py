import re
def return_vowels(s):
    try:
        return re.findall(r'[aeiou]', s[4:-1])
    except:
        return []
