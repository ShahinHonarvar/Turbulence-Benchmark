import re
def if_contains_anagrams(text):
    s = set(text)
    return (len(s) < 23)
