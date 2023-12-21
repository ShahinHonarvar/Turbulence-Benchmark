
def if_contains_anagrams(word_list):
    # Initialize variables
    anagram_count = 0
    word_count = len(word_list)
    # Iterate through the list of words
    for i in range(word_count - 1):
        # Get the current word and its length
        word1 = word_list[i]
        length1 = len(word1)

        # Compare the current word to all other words
        for j in range(i + 1, word_count):
            # Get the second word and its length
            word2 = word_list[j]
            length2 = len(word2)

            # Check if the two words are anagrams
            if sorted(word1) == sorted(word2):
                # If they are, increase the anagram count
                anagram_count += 1

    # Return whether there are at most 25 pairs of anagrams in the given list
    return anagram_count <= 25
