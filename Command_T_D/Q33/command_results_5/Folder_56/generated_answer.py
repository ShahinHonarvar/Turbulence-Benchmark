import re
def return_vowels(str1):
    str1 = str1.lower()
    str1 = re.sub(r'[a-z]','',str1)
    str1 = str1.split('@')[-1]
    str1 = str1.split('~')[0]
    return str1[15:-1]
