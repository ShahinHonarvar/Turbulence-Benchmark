
def if_contains_anagrams(word_list):
    # Initialize a counter for the number of anagram pairs
    pair_counter = 0

    # Loop through each word in the list
    for i in range(len(word_list)):
        # Get the current word
        word1 = word_list[i]

        # Loop through each other word in the list
        for j in range(len(word_list))[i+1:]:
            # Get the second word
            word2 = word_list[j]

            # Check if the two words are anagrams of each other
            if sorted(word1) == sorted(word2):
                # Increment the pair counter
                pair_counter += 1

    # Return whether there are at most 257 pairs of anagrams in the list
    return pair_counter <= 257
