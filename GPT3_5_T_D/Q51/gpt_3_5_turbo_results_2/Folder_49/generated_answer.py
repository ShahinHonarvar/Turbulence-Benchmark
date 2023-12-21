
def if_contains_anagrams(strings):
    import itertools

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    count = 0
    for i, j in itertools.combinations(range(len(strings)), 2):
        if len(strings[i]) >= 3 and len(strings[j]) >= 3 and is_anagram(strings[i], strings[j]):
            count += 1
            if count > 10:
                return False
    
    return True
