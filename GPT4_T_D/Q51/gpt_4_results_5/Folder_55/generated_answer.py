
from collections import defaultdict

def if_contains_anagrams(words):
    words = [word.lower() for word in words if len(word) >= 3]
    counter = defaultdict(int)
    for word in words:
        sorted_word = ''.join(sorted(word))
        counter[sorted_word] += 1
    pairs_count = sum([value // 2 for value in counter.values()])
    return pairs_count <= 44
