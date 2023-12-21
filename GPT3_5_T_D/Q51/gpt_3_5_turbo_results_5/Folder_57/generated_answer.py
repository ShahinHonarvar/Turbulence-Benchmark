
def if_contains_anagrams(string_list):
    import itertools
    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    
    count = 0
    for pair in itertools.combinations(string_list, 2):
        if is_anagram(pair[0], pair[1]) and len(pair[0]) >= 3:
            count += 1
            if count > 74:
                return False
    return True
