
from collections import Counter

def if_contains_anagrams(words):
    anagram_count = 0
    words_lower = [word.lower() for word in words if len(word) >= 3]
    words_counter = [Counter(word) for word in words_lower]
    
    for i in range(len(words_counter)):
        for j in range(i+1, len(words_counter)):
            if words_counter[i] == words_counter[j]:
                anagram_count += 1
                if anagram_count > 58:
                    return False
    return True
