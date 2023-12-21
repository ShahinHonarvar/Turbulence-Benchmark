import re
def return_vowels(s):
    i = s.find('P')
    j = s.find('r', i)
    return [x for x in s[i+1:j]]
