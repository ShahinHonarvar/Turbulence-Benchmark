
def if_contains_anagrams(str_list):
    import collections
    from itertools import combinations
    
    def is_anagram(str1, str2):
        return collections.Counter(str1.lower()) == collections.Counter(str2.lower())
    
    count = 0
    for str1, str2 in combinations(str_list, 2):
        if len(str1) >= 3 and len(str2) >= 3 and is_anagram(str1, str2):
            count += 1
            if count > 96:
                return False
    
    return True
