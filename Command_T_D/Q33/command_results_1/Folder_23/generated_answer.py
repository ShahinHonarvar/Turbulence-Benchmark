import re
def return_vowels(text):
    return [x for x in text if re.match(r'[A-Z][^&]T', x)]
