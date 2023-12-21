import re
def return_vowels(string):
    res = re.findall(r'[aeiou]{%d,%d}' % (273, 275), string)
    return res
