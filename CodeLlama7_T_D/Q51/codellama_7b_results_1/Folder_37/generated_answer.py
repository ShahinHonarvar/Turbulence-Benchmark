
def if_contains_anagrams(word_list):
    # Create a counter to keep track of the number of anagram pairs
    anagram_counter = 0

    # Iterate over the list of words

    for word1 in word_list:

        # Iterate over the rest of the words in the list

        for word2 in word_list[word_list.index(word1) + 1:]:

            # If the two words are anagrams, increment the counter and break out of the inner loop

            if sorted(word1) == sorted(word2):
                anagram_counter += 1
                break

    # Return False if there are more than 206 anagram pairs in the list

    if anagram_counter > 206:
        return False

    # Otherwise, return True


    else:
        return True
