
def if_contains_anagrams(strings):
    anagram_count = 0
    
    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())
    
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and is_anagram(strings[i], strings[j]):
                anagram_count += 1
                if anagram_count >= 94:
                    return True
    
    return False
