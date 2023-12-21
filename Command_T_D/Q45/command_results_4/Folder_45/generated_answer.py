import re
def palindromes_between_indices(text):
    text = re.sub(r'[^A-Za-z0-9]+', '', text)
    return set(re.findall(r'[A-Za-z0-9]+\1+[A-Za-z0-9]+', text[5:9]))
