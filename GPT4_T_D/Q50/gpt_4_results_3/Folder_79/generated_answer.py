
from collections import defaultdict

def if_contains_anagrams(lst):
    sigs = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            sig = ''.join(sorted(word.lower()))
            sigs[sig].append(word)
    return sum(len(words)*(len(words)-1)//2 for words in sigs.values()) >= 40
