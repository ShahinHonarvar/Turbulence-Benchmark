
def if_contains_anagrams(my_list):
    anagram_count = 0
    for i in range(len(my_list)):
        word1 = my_list[i].lower()
        for j in range(i+1, len(my_list)):
            word2 = my_list[j].lower()
            if len(word1) >= 3 and len(word2) >= 3:
                anagram_count += int(sorted(word1) == sorted(word2))
    return anagram_count >= 123
