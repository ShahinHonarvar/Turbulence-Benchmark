import re
def return_vowels(str1):
    str1 = str(str1)
    str1 = re.sub(r'[^A-Z]', '', str1)
    str1 = str1[170:403]
    if len(str1) == 0:
        return []
    str1 = str1.split('')
    str1 = [x for x in str1 if x in 'AEIOU']
    return str1
