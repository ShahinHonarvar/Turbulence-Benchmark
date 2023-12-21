
def if_contains_anagrams(my_list):
    anagram_pairs = 0
    for i in range(len(my_list)):
        word1 = my_list[i].lower()
        for j in range(i + 1, len(my_list)):
            word2 = my_list[j].lower()
            if len(word1) >= 3 and len(word2) >= 3:
                if sorted(word1) == sorted(word2):
                    anagram_pairs += 1
                    if anagram_pairs > 75:
                        return False
    return True
