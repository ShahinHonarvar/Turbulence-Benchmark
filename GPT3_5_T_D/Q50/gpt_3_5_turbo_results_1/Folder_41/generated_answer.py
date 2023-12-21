
def if_contains_anagrams(strings):
    from collections import Counter
    
    def is_anagram(word1, word2):
        return Counter(word1.lower()) == Counter(word2.lower())
    
    count = 0
    for i in range(len(strings) - 1):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and is_anagram(strings[i], strings[j]):
                count += 1
                if count >= 75:
                    return True
                
    return False
