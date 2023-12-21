import re
def return_vowels(str1):
    str1 = re.sub(r'[^A-Z]','',str1)
    return [x for x in str1[24:59]]
