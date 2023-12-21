import re
def return_vowels(s):
    for m in re.finditer(r'<(.)>{23}(?<=.)<(d)', s):
        yield m.group(1)
