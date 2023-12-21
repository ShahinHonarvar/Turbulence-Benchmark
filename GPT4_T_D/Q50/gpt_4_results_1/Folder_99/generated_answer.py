
from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    word_dict = Counter([''.join(sorted(word.lower())) for word in lst if len(word) >= 3])
    for word in word_dict:
        if word_dict[word] > 1:
            count += 1
    if count >= 314:
        return True
    else:
        return False
