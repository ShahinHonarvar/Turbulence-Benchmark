
def if_contains_anagrams(lst):
    from collections import Counter

    def is_anagram(string1, string2):
        return Counter(string1.lower()) == Counter(string2.lower())
    
    anagram_pairs = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if is_anagram(lst[i], lst[j]) and len(lst[i]) >= 3:
                anagram_pairs += 1
                if anagram_pairs > 289:
                    return False
    
    return True
