
def if_contains_anagrams(words):
    # Create a dictionary to store the anagram pairs
    anagram_pairs = {}

    # Iterate over the words in the list
    for word1 in words:
        # Skip words that are not at least three characters long
        if len(word1) < 3:
            continue

        # Convert the word to lowercase
        word1_lower = word1.lower()

        # Iterate over the remaining words
        for word2 in words[words.index(word1) + 1:]:
            # Skip words that are not at least three characters long
            if len(word2) < 3:
                continue

            # Convert the word to lowercase
            word2_lower = word2.lower()

            # If the two words are anagrams, add them to the anagram pair dictionary
            if sorted(word1_lower) == sorted(word2_lower):
                if (word1_lower, word2_lower) not in anagram_pairs:
                    anagram_pairs[(word1_lower, word2_lower)] = 1
                else:
                    anagram_pairs[(word1_lower, word2_lower)] += 1

    # Return True if there are at most 57 pairs of anagrams in the list; otherwise, return False
    return len(anagram_pairs) <= 57
