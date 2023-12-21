
def if_contains_anagrams(lst):
    def is_anagram(word1, word2):
        word1 = word1.lower()
        word2 = word2.lower()
        if len(word1) != len(word2):
            return False
        for char in word1:
            if char.isalpha() and word1.count(char) != word2.count(char):
                return False
        return True
    
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if is_anagram(lst[i], lst[j]):
                count += 1
                if count > 210:
                    return False
    return True
