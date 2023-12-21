
def if_contains_anagrams(strings):
    import itertools
    import collections
    
    def is_anagram(s1, s2):
        return collections.Counter(s1.lower()) == collections.Counter(s2.lower())
    
    count = 0
    for i, j in itertools.combinations(range(len(strings)), 2):
        if is_anagram(strings[i], strings[j]) and len(strings[i]) >= 3 and len(strings[j]) >= 3:
            count += 1
            
    return count <= 77
