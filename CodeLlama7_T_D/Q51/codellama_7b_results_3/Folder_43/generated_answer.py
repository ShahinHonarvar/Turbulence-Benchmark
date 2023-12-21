
def if_contains_anagrams(words):
    anagram_pairs = []
    for word1 in words:
        for word2 in words:
            if len(word1) >= 3 and len(word2) >= 3:
                if sorted(word1.lower()) == sorted(word2.lower()):
                    anagram_pairs.append((word1, word2)))
    return len(anagram_pairs) <= 3
