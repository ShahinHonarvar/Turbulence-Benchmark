
def if_contains_anagrams(strings):
    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())
    
    anagram_pairs = 0
    for i in range(len(strings)-1):
        for j in range(i+1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and is_anagram(strings[i], strings[j]):
                anagram_pairs += 1
                if anagram_pairs >= 3:
                    return True
    return False
