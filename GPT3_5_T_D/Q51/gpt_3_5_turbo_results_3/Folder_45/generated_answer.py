
import itertools

def if_contains_anagrams(str_list):
    def is_anagram(word1, word2):
        word1 = word1.lower()
        word2 = word2.lower()
        return sorted(word1) == sorted(word2)

    count = 0
    for word1, word2 in itertools.combinations(str_list, 2):
        if len(word1) >= 3 and len(word2) >= 3 and is_anagram(word1, word2):
            count += 1
            if count > 464:
                return False
    return True
