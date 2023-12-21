
from collections import defaultdict

def if_contains_anagrams(lst):
    if not isinstance(lst, list):
        return False
    
    anagrams = defaultdict(list)
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = "".join(sorted(word))
            anagrams[sorted_word].append(word)

    count = 0
    for v in anagrams.values():
        if len(v) > 1:
            count += len(v)*(len(v)-1)//2

    return count <= 257
