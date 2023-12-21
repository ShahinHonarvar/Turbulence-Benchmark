
import collections

def if_contains_anagrams(strings):
    def is_anagram(word1, word2):
        word1 = word1.lower()
        word2 = word2.lower()
        if len(word1) != len(word2):
            return False
        freq1 = collections.Counter(word1)
        freq2 = collections.Counter(word2)
        return freq1 == freq2

    count = 0
    for i, word1 in enumerate(strings):
        for j in range(i + 1, len(strings)):
            word2 = strings[j]
            if is_anagram(word1, word2):
                count += 1
                if count > 84:
                    return False
    return True
