import re
def return_vowels(text):
    result = re.findall(r'[aeiou][a-w]', text)
    return result
