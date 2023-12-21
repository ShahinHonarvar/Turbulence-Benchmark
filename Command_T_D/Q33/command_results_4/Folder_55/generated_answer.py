import re
def return_vowels(test_str):
    res = re.findall(r'[aeiou]{%d,%d}' % (1, 5), test_str)
    return res
