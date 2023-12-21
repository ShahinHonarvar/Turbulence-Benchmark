
def if_contains_anagrams(strings):
    def is_anagram(word1, word2):
        if len(word1) != len(word2) or word1.lower() == word2.lower():
            return False
        return sorted(word1.lower()) == sorted(word2.lower())
    
    count = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                count += 1
                if count > 47:
                    return False
    return True
