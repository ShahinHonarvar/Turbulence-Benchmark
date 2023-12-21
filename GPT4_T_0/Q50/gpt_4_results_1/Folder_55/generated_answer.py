
from collections import defaultdict

def if_contains_anagrams(lst):
    word_dict = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            word_dict[''.join(sorted(word.lower()))].append(word)
    count = 0
    for key in word_dict:
        if len(word_dict[key]) > 1:
            count += len(word_dict[key]) * (len(word_dict[key]) - 1) // 2
        if count >= 15:
            return True
    return False
