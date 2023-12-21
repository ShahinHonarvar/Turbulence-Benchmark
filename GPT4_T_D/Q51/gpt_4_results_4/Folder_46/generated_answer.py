
def if_contains_anagrams(lst):
    from collections import defaultdict
    
    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    anagrams = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            anagrams[''.join(sorted(word.lower()))].append(word)
            
    anagram_pairs = sum(len(v)*(len(v)-1)//2 for v in anagrams.values())
    
    if anagram_pairs <= 61:
        return True
    return False
