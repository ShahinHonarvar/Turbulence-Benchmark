
from collections import Counter

def is_anagram(w1, w2):
    return Counter(w1.lower()) == Counter(w2.lower())

def if_contains_anagrams(lst):
    pairs = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and is_anagram(lst[i], lst[j]):
                pairs.append((lst[i], lst[j]))
                if len(pairs) > 16:
                    return False
    return True
