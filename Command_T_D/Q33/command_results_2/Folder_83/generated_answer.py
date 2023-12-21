import re
def return_vowels(text):
    text = re.sub(r'[a-z]','',text)
    return list(filter(str.isalpha, list(range(ord('a')+1, ord('z')+1))))
