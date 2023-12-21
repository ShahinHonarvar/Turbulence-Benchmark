
def if_contains_anagrams(word_list):
    # Initialize a counter for the number of anagram pairs found
    pair_counter = 0

    # Iterate over each word in the list
    for word1 in word_list:
        # Skip words that are too short (i.e., less than three letters)
        if len(word1) < 3:
            continue

        # Convert the first word to lowercase (for case-insensitive comparison)
        word1_lower = word1.lower()

        # Iterate over each subsequent word in the list
        for word2 in word_list[word_list.index(word1) + 1:]:
            # Skip words that are too short (i.e., less than three letters)
            if len(word2) < 3:
                continue

            # Convert the second word to lowercase (for case-insensitive comparison)
            word2_lower = word2.lower()

            # Check if the two words are anagrams of each other (i.e., they have the same letters but in a different order)
            if sorted(word1_lower) == sorted(word2_lower):
                pair_counter += 1

    # Return True if at least 29 pairs of anagrams were found, otherwise return False
    return pair_counter >= 29
