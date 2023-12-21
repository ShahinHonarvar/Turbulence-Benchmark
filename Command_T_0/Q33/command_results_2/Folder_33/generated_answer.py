import re
def return_vowels(s):
    return re.findall(r'[A-E][^:]+', s)[1:-1]
