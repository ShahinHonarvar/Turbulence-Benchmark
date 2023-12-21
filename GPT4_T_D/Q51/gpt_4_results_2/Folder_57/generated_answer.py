
from collections import Counter

def if_contains_anagrams(string_list):

    # Function to generate a character frequency map for the given string
    def create_frequency_map(s):
        return Counter(s.lower())

    # Function to check if two strings are anagrams
    def are_anagrams(s1, s2):
        return create_frequency_map(s1) == create_frequency_map(s2)

    anagram_pairs = 0
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            if len(string_list[i]) >= 3 and len(string_list[j]) >= 3:
                if are_anagrams(string_list[i], string_list[j]):
                    anagram_pairs += 1
                    if anagram_pairs > 74:
                        return False
    return True
