
def if_contains_anagrams(my_list):
    # create a dictionary to store the anagram counts
    anagram_counts = {}

    for word in my_list:
        # convert the word to lowercase
        word = word.lower()

        # check if the word is at least three letters long
        if len(word) >= 3:
            # create a sorted version of the word
            sorted_word = "".join(sorted(word))

            # check if the sorted word has been seen before
            if sorted_word in anagram_counts:
                # increment the count for this anagram
                anagram_counts[sorted_word] += 1

            else:
                # add a new entry to the dictionary
                anagram_counts[sorted_word] = 1

    # check if there are at most four pairs of anagrams in the list
    return len(anagram_counts) <= 4
