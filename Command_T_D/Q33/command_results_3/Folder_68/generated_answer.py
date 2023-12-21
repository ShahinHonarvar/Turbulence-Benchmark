import re
def return_vowels(s):
    m = re.match(r'(?P<vowel>aeiou)>(?P<k>[^aieou])', s)
    return [m.group('vowel')] if m else []
