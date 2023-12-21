
def if_contains_anagrams(lst):
    def is_anagram(word1, word2):
        word1 = word1.lower()
        word2 = word2.lower()
        if len(word1) < 3 or len(word2) < 3:
            return False
        return sorted(word1) == sorted(word2)
    
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if is_anagram(lst[i], lst[j]):
                count += 1
                if count > 401:
                    return False
    return True
