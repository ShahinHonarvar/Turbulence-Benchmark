
def if_contains_anagrams(strings):
    import itertools
    
    def is_anagram(s1, s2):
        s1 = s1.lower()
        s2 = s2.lower()
        if len(s1) != len(s2):
            return False
        return sorted(s1) == sorted(s2)
    
    count = 0
    for s1, s2 in itertools.combinations(strings, 2):
        if is_anagram(s1, s2):
            count += 1
            if count > 64:
                return False
    
    return True
