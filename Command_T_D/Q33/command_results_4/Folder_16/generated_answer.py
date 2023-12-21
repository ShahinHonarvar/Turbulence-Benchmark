import re
def return_vowels(s):
    return re.findall(r'([aeiou])([^aieou])', s[133:-1])
