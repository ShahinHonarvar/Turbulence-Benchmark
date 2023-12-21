import re
def return_vowels(s):
    return re.findall(r'[aeiou][^z]', s)[56:-1]
