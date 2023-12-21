
from collections import Counter

def if_contains_anagrams(lst):
    def is_anagram(s, t):
        return Counter(s) == Counter(t)
    
    strings = [''.join(sorted(word.lower())) for word in lst if len(word) >= 3]
    
    anagram_count = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagram_count += 1
                if anagram_count > 81:
                    return False
    return True
