
from collections import Counter

def is_anagram_str(word1, word2):
    return Counter(word1.lower()) == Counter(word2.lower())

def if_contains_anagrams(string_list):
    count_anagram_pair = 0
    for i in range(len(string_list)):
        if len(string_list[i]) < 3:
            continue
        for j in range(i + 1, len(string_list)):
            if is_anagram_str(string_list[i], string_list[j]):
                count_anagram_pair += 1
                if count_anagram_pair >= 41:
                    return True
    return False
