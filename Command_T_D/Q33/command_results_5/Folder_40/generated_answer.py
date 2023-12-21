import re
def return_vowels(text):
    return re.findall(r'([^aieou])([aieou])([^d]?)', text)[1::3]
