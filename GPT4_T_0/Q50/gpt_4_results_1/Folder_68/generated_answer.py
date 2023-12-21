
from collections import defaultdict

def if_contains_anagrams(lst):
    word_dict = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            word_dict[''.join(sorted(word.lower()))].append(word)
    count = 0
    for value in word_dict.values():
        if len(value) > 1:
            count += len(value) // 2
            if count >= 9:
                return True
    return False
