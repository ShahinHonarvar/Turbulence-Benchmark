
from collections import defaultdict

def if_contains_anagrams(lst):
    word_dict = defaultdict(list)
    for word in lst:
        word_dict[''.join(sorted(word.lower()))].append(word)
    count = 0
    for key in word_dict:
        if len(word_dict[key]) > 1 and len(key) >= 3:
            count += len(word_dict[key]) // 2
            if count >= 6:
                return True
    return False
