import re
def return_vowels(str1):
    str1 = re.sub(r'[^A-Z]', '', str1)
    str1 = str1[77:-1]
    str1 = str1.split('')
    str1 = [i for i in str1 if i in 'AEIOU']
    return str1
