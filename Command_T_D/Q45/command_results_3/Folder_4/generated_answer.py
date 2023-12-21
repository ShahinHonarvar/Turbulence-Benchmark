import re
def palindromes_between_indices(text):
    try:
        letters = text[3:9].lower()
        return set(re.findall(r'[a-z]{7}'.format(7), letters))
    except:
        return set()
