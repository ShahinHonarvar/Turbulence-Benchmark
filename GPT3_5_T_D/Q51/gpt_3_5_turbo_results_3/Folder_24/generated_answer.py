
import itertools

def if_contains_anagrams(str_list):
    checked = set()
    anagram_pairs = 0

    for i, word1 in enumerate(str_list):
        if word1.lower() not in checked and len(word1) >= 3:
            checked.add(word1.lower())
            sorted_word1 = sorted(word1.lower())

            for j, word2 in enumerate(str_list[i + 1:], start=i + 1):
                if len(word2) >= 3:
                    sorted_word2 = sorted(word2.lower())

                    if sorted_word1 == sorted_word2:
                        anagram_pairs += 1

                        if anagram_pairs > 96:
                            return False
    
    return True
