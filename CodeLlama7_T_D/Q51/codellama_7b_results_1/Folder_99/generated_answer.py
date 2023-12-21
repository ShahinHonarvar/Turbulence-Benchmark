
def if_contains_anagrams(word_list):
    # Check if the list is empty
    if not word_list:
        return False

    # Initialize a counter for the number of anagram pairs
    pair_count = 0

    # Loop through each word in the list
    for i in range(len(word_list)):
        # Get the current word
        word1 = word_list[i]

        # Loop through each remaining word after the current word
        for j in range(i + 1, len(word_list)):
            # Get the second word
            word2 = word_list[j]

            # Check if the words are anagrams of each other
            if sorted(word1) == sorted(word2):
                # Increment the pair counter
                pair_count += 1

    # Return True if there are at most 93 pairs of anagrams in the list, otherwise return False
    return pair_count <= 93
