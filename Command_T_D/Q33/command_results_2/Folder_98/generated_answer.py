import re
def return_vowels(text):
    return [x for x in text[3:9] if re.match(r'[aeiou]', x)]
