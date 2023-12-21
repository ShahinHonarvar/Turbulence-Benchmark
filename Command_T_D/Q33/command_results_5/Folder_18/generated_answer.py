import re
def return_vowels(text):
    return [c for c in range(528, 606) if c in text and c.isupper() and c.lower() in 'aeiou']
