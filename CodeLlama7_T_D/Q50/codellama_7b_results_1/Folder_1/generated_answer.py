
def if_contains_anagrams(words):
    # Initialize variables for counting anagrams
    num_anagrams = 0
    min_word_length = 3

    # Iterate over the words in the list
    for word1 in words:
        # Skip words that are too short to be anagrams
        if len(word1) < min_word_length:
            continue

        # Create a sorted version of the word
        sorted_word = "".join(sorted(word1))

        # Iterate over the remaining words in the list
        for word2 in words[words.index(word1)+1:]:
            # Skip words that are too short to be anagrams
            if len(word2) < min_word_length:
                continue

            # If the sorted versions of the two words match, they are anagrams
            if "".join(sorted(word2)) == sorted_word:
                num_anagrams += 1

    # Return True if there are at least 96 pairs of anagrams in the list, otherwise return False
    return num_anagrams >= 96
