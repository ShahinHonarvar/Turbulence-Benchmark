import re
def return_vowels(text):
    return re.findall(r'[aeiou]', text[50:51])
