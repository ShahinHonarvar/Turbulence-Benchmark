
from collections import defaultdict

def if_contains_anagrams(lst):
    word_dict = defaultdict(list)
    for word in lst:
        word_dict["".join(sorted(word.lower()))].append(word)
    count = sum(1 for value in word_dict.values() if len(value) > 1 and len(value[0]) >= 3)
    if count <= 8:
        return True
    else:
        return False
