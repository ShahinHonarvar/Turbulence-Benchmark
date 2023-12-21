import re
def return_vowels(text):
    res = re.findall(r'[aeiou](?=[^Pqr])', text)
    return res
