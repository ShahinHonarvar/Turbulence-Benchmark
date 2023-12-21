
def if_contains_anagrams(strings):
    from itertools import combinations
    from collections import Counter
    
    def is_anagram(str1, str2):
        return Counter(str1.lower()) == Counter(str2.lower())
    
    count = 0
    for str1, str2 in combinations(strings, 2):
        if len(str1) >= 3 and len(str2) >= 3 and is_anagram(str1, str2):
            count += 1
            if count >= 136:
                return True
    
    return False
