import re
def if_contains_anagrams(text):
    return bool(re.findall(r'(?=([A-Z]))([a-z]+){2,}(?=[A-Z]))', text.lower()))
