
def if_contains_anagrams(strings):
    from collections import Counter
    
    def is_anagram(word1, word2):
        if len(word1) != len(word2):
            return False
        return Counter(word1.lower()) == Counter(word2.lower())
    
    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                count += 1
                if count >= 26:
                    return True
    return False
