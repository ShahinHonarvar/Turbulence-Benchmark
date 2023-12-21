
from collections import Counter

def if_contains_anagrams(strings):
    def is_anagram(word1, word2):
        word1_count = Counter(word1.lower())
        word2_count = Counter(word2.lower())
        return word1_count == word2_count
    
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and is_anagram(strings[i], strings[j]):
                anagram_pairs += 1
                if anagram_pairs > 30:
                    return False
    
    return True
