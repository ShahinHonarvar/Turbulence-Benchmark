
from collections import Counter
from itertools import combinations

def if_contains_anagrams(str_list):
    anagrams = [str.lower() for str in str_list if len(str)>=3]
    anagrams = [''.join(sorted(word)) for word in anagrams]
    count = Counter(anagrams)

    pairs = 0
    for val in count.values():
        pairs += sum(range(val))

    if pairs <= 60:
        return True
    else:
        return False
