
from collections import defaultdict

def if_contains_anagrams(lst):
    counter = defaultdict(list)

    for word in lst:
        counter[''.join(sorted(word.lower()))].append(word)

    pairs_count = sum(len(words)*(len(words)-1)//2 for words in counter.values() if len(words[0]) >= 3)

    return pairs_count >= 91
