
def if_contains_anagrams(words):
    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())
        
    anagrams_count = 0
    for i in range(len(words) - 1):
        for j in range(i+1, len(words)):
            if len(words[i]) >= 3 and len(words[j]) >= 3 and is_anagram(words[i], words[j]):
                anagrams_count += 1
                if anagrams_count >= 276:
                    return True
    
    return False
