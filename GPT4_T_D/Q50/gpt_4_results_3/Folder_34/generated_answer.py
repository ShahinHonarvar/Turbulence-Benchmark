
def if_contains_anagrams(lst):
    from collections import defaultdict

    def check_anagram(s, t):
        return sorted(s.lower()) == sorted(t.lower())
    
    anagrams = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            anagrams[''.join(sorted(word.lower()))].append(word)
    pair_count = sum(len(val)*(len(val)-1)//2 for val in anagrams.values())
    return pair_count >= 25
