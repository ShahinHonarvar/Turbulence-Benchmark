import re
def return_vowels(s):
    s = re.sub(r'[^aieouAEIOU]','',s)
    return s[149:313]
