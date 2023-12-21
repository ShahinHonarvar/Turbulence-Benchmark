import re
def return_vowels(text):
    return re.findall(r'[A-Z][aeiou]', text[11:-1])
