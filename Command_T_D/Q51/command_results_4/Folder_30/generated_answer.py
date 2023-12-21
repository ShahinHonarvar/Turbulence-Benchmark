import re
def if_contains_anagrams(texts):
    return len(re.findall(r'(?=([a-z]))([a-z][^a-z]*[a-z]', texts)) <= 28
