
from collections import defaultdict

def if_contains_anagrams(words):
    def count_anagrams(words):
        d = defaultdict(list)
        for word in words:
            d[''.join(sorted(word.lower()))].append(word)
        return d

    def count_pairs(lst):
        return len(lst) * (len(lst) - 1) // 2
    
    d = count_anagrams(words)    
    anagram_pairs = [count_pairs(v) for k, v in d.items() if len(v) > 1 and len(k) >= 3]    
    return sum(anagram_pairs) <= 97
