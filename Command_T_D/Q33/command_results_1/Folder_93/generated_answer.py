import re
def return_vowels(str1):
    str1 = re.sub(r'[^A-Z0-9]', '', str1)
    str1 = str1[54:82]
    if len(str1) > 0:
        return str1
    else:
        return []
