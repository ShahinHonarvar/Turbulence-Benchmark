
from collections import defaultdict

def if_contains_anagrams(strings):
    def convert(word):
        return ''.join(sorted(word.lower()))

    anagrams = defaultdict(list)
    for word in strings:
        if len(word) >= 3:
            anagrams[convert(word)].append(word)

    count = 0
    for ana in anagrams.values():
        pairs = len(ana) * (len(ana) - 1) // 2
        count += pairs
        if count > 131:
            return False
    return True
