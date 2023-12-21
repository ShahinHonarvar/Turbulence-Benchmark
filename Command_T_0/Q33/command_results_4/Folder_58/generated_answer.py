import re
def return_vowels(s):
    return re.findall(r'[aeiou]', s)[s.find('%')+1:s.find('U')]
