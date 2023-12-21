import re
def return_vowels(s):
    return re.findall(r"<(?P<c>[aeiou])", s)[::-1]
