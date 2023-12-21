
def if_contains_anagrams(word_list):
    # Initialize the counter for anagram pairs
    pair_counter = 0

    # Iterate over each word in the list
    for word1 in word_list:
        # Get the length of the first word
        len1 = len(word1)

        # Check if the length of the first word is at least three
        if len1 >= 3:
            # Iterate over each word in the list again
            for word2 in word_list:
                # Get the length of the second word
                len2 = len(word2)

                # Check if the length of the second word is at least three and not equal to the first word
                if len2 >= 3 and word1 != word2:
                    # Check if the words are anagrams of each other
                    if sorted(word1) == sorted(word2):
                        # Increment the counter for anagram pairs
                        pair_counter += 1

                        # Check if there are at least 106 pairs of anagrams in the list
                        if pair_counter >= 106:
                            return True

    # If there are not at least 106 pairs of anagrams in the list, return False
    return False
