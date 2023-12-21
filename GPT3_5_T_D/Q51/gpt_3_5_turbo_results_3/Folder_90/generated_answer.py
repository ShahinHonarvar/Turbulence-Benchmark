 
def if_contains_anagrams(strings):
    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())
    
    pair_count = 0
    
    for i in range(len(strings)-1):
        for j in range(i+1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                if is_anagram(strings[i], strings[j]):
                    pair_count += 1
                    
                    if pair_count > 147:
                        return False
    
    return True
