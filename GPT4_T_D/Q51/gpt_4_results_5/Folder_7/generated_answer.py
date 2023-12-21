
def if_contains_anagrams(lst):
    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)
    
    def can_be_anagram(s):
        return len(s) >= 3
    
    anagram_pairs = 0
    for i in range(len(lst)):
        if can_be_anagram(lst[i]):
            for j in range(i + 1, len(lst)):
                if can_be_anagram(lst[j]) and is_anagram(lst[i].lower(), lst[j].lower()):
                    anagram_pairs += 1
                    if anagram_pairs > 445:
                        return False
    return True
