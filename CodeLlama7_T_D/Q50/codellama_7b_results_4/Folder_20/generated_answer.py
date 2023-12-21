
def if_contains_anagrams(words):
    # Check if the length of the list is at least 64
    if len(words) < 64:
        return False

    # Create a dictionary to store the anagram pairs
    anagram_pairs = {}

    # Iterate over the words in the list
    for word1 in words:

        # Iterate over the words again, but start from the next word
        for word2 in words[words.index(word1) + 1:]:

            # If the two words are anagrams, add them to the dictionary
            if sorted(word1) == sorted(word2):
                anagram_pairs[(word1, word2)] = True

    # Return True if there are at least 64 pairs of anagrams in the list, False otherwise
    return len(anagram_pairs) >= 64
