
def if_contains_anagrams(str_list):
    def is_anagram(word1, word2):
        word1 = word1.lower().replace(" ", "")
        word2 = word2.lower().replace(" ", "")
        if len(word1) != len(word2):
            return False
        for char in word1:
            if char not in word2:
                return False
        return True
    
    count = 0
    for i in range(len(str_list)):
        for j in range(i+1, len(str_list)):
            if is_anagram(str_list[i], str_list[j]):
                count += 1
                if count > 34:
                    return False
    
    return True
