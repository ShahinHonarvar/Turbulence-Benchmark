
def if_contains_anagrams(lst):
    from collections import defaultdict
    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    
    anagram_pairs = defaultdict(list)
    
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_pairs[sorted_word].append(word)
    
    pairs_sum = sum(len(v)*(len(v)-1)//2 for v in anagram_pairs.values())
    
    return pairs_sum >= 140
