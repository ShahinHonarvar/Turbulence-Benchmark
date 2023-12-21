import re
def return_vowels(s):
    for m in re.finditer(r'<(?P<vowel>aieouAEIOU)[^<]*>(?P=vowel)>', s):
        yield m.group(1)
