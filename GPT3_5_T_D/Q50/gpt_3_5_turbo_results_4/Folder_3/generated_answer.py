
import itertools

def if_contains_anagrams(strings):
    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())

    anagram_count = 0
    for pair in itertools.combinations(strings, 2):
        if len(pair[0]) >= 3 and len(pair[1]) >= 3 and is_anagram(pair[0], pair[1]):
            anagram_count += 1
            if anagram_count >= 30:
                return True

    return False
