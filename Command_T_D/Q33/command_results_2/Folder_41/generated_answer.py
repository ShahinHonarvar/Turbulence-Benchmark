import re
def return_vowels(text):
    text = re.sub(r"[^A-Z]","",text)
    return [i for i in range(72,83) if text[i-72] in 'AEIOU']
