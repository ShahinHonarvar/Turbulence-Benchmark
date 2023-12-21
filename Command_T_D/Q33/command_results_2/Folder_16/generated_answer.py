import re
def return_vowels(s):
    s = re.sub(r'[^aieou]', '', s)
    return s[133:-1]
