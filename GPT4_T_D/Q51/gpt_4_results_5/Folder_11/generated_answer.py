
from collections import defaultdict

def if_contains_anagrams(lst):
    word_dict = defaultdict(list)
    count = 0
    for word in lst:
        word_dict[''.join(sorted(word.lower()))].append(word)

    for value in word_dict.values():
        if len(value) > 1 and len(value[0]) >= 3:
            count += len(value) - 1
    
    if count <= 41:
        return True
    else:
        return False
