import re
def return_vowels(text):
    text = text[604:949]
    m = re.search("(?!.)([aeiou])", text)
    return list(m.group())
