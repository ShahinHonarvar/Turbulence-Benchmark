
def if_contains_anagrams(my_list):
    anagram_pairs = 0
    for i in range(len(my_list)):
        word1 = my_list[i].lower()
        for j in range(i+1, len(my_list)):
            word2 = my_list[j].lower()
            if is_anagram(word1, word2):
                anagram_pairs += 1
    return anagram_pairs <= 42

def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2) and len(word1) >= 3 and len(word2) >= 3
