
def if_contains_anagrams(words):
    # Create a set of all anagram pairs
    anagram_pairs = set()
    for word1 in words:
        for word2 in words:
            if len(word1) < 3 or len(word2) < 3:
                continue

            if sorted(word1.lower()) == sorted(word2.lower()):
                anagram_pairs.add((word1, word2))
    # Check if there are more than 4 pairs of anagrams
    return len(anagram_pairs) <= 4
