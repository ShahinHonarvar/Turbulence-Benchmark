
from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for word in lst:
        anagrams[''.join(sorted(word.lower()))].append(word)
    pairs = 0
    for word_list in anagrams.values():
        if len(word_list) > 1:
            for i in range(len(word_list)):
                for j in range(i+1, len(word_list)):
                    # check if word length is at least 3
                    if len(word_list[i]) >= 3 and len(word_list[j]) >= 3:
                        pairs += 1
                        if pairs > 34:
                            return False
    return True
