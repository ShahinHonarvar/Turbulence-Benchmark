import re
def return_vowels(s):
    s = re.sub(r'[^A-Za-z]','',s)
    s = s[323:-1]
    s = re.sub(r'[^AEIOUaeiou]','',s)
    return s
