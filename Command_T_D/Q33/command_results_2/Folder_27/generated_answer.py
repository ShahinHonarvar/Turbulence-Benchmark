import re
def return_vowels(s):
    return re.findall(r'([eio][^aieuf])', s)[1:-1]
