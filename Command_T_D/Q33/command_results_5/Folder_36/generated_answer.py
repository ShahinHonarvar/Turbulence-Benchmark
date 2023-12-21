import re
def return_vowels(str1):
    str1 = str1[604:]
    str1 = str1[:949]
    str1 = re.sub(r'[^A-Z]', '', str1)
    str1 = str1.split('')
    return [i for i in str1 if i in 'AEIOU']
