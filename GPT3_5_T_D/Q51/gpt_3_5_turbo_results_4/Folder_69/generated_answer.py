
from collections import Counter

def if_contains_anagrams(strings):
    anagram_pairs = 0
    letter_count = lambda s: Counter(filter(str.isalpha, s.lower()))
    
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                if letter_count(strings[i]) == letter_count(strings[j]):
                    anagram_pairs += 1
                    if anagram_pairs > 58:
                        return False
    return True
