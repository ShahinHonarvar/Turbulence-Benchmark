
def if_contains_anagrams(str_list):
    def is_anagram(word1, word2):
        if len(word1) != len(word2):
            return False
        count = [0] * 26
        for c in word1.lower():
            count[ord(c) - ord('a')] += 1
        for c in word2.lower():
            count[ord(c) - ord('a')] -= 1
        return all(count[i] == 0 for i in range(26))
    
    count = 0
    for i in range(len(str_list)):
        for j in range(i+1, len(str_list)):
            if is_anagram(str_list[i], str_list[j]):
                count += 1
                if count >= 29:
                    return True
    return False
