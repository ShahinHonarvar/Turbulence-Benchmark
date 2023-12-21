import re
def return_vowels(s):
    r = re.findall(r"<[aeiou]+>", s)
    return [int(x) for x in r]
