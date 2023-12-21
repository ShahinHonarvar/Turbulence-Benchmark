
def if_contains_anagrams(word_list):
    # Initialize variables
    anagram_count = 0
    three_letter_anagrams = []

    # Iterate over the words in the list
    for word1 in word_list:
        # Ignore words that are less than three letters
        if len(word1) < 3:
            continue

        # Create a copy of the word with all lowercase letters
        word1_lower = word1.lower()

        # Iterate over the remaining words in the list
        for word2 in word_list[word_list.index(word1) + 1:]:
            # Ignore words that are less than three letters
            if len(word2) < 3:
                continue

            # Create a copy of the word with all lowercase letters
            word2_lower = word2.lower()

            # Check if the two words are anagrams
            if sorted(word1_lower) == sorted(word2_lower):
                # Increment the anagram count
                anagram_count += 1

                # Add the two anagrams to a list of three-letter anagrams
                three_letter_anagrams.append((word1, word2)))

    # Return true if there are at least 188 pairs of anagrams in the given list; otherwise, return false
    return anagram_count >= 188
