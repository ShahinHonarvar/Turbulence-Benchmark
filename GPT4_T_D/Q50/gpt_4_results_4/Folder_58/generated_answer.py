
def if_contains_anagrams(lst):
    from itertools import combinations
    from collections import defaultdict
    
    def is_anagram(st1, st2):
        return sorted(st1.lower()) == sorted(st2.lower())
    
    count = 0
    words = [w for w in lst if len(w) >= 3]
    for word1, word2 in combinations(words, 2):
        if is_anagram(word1, word2):
            count += 1
    return count >= 411
