
def if_contains_anagrams(str_list):
    def is_anagram(word1, word2):
        if len(word1) != len(word2):
            return False
        word1 = word1.lower()
        word2 = word2.lower()
        return sorted(word1) == sorted(word2)

    anagram_count = 0
    for i in range(len(str_list)-1):
        for j in range(i+1, len(str_list)):
            if is_anagram(str_list[i], str_list[j]):
                anagram_count += 1
                if anagram_count >= 98:
                    return True
    return False
