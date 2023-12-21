
def if_contains_anagrams(lst):
    from collections import Counter
    
    def is_anagram(s1, s2):
        s1_count = Counter(s1.lower())
        s2_count = Counter(s2.lower())
        return s1_count == s2_count
    
    anagram_pairs = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and is_anagram(lst[i], lst[j]):
                anagram_pairs += 1
                if anagram_pairs > 52:
                    return False
    return True
