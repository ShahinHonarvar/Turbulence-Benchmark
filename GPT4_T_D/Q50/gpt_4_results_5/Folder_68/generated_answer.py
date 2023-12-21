
from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(list)
    for word in lst:
        if len(word)>=3:
            d[''.join(sorted(word.lower()))].append(word)
    pairs = sum([len(value_list)*(len(value_list) - 1)//2 for value_list in d.values() if len(value_list) > 1])
    return pairs >= 9
