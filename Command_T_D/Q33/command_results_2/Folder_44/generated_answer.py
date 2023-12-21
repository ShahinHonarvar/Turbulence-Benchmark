import re
def return_vowels(s):
    for m in re.finditer(r'[aeiou](?![aieou])', s):
        yield m.group()
