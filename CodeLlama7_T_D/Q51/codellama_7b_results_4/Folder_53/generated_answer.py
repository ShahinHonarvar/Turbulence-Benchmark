
def if_contains_anagrams(my_list):
    # create a dictionary to store the anagram counts
    anagram_counts = {}

    for word in my_list:
        # convert the word to lowercase
        word = word.lower()

        # sort the letters of the word
        sorted_word = ''.join(sorted(word))

        # check if the anagram count for this sorted word is greater than 8
        if anagram_counts.get(sorted_word, 0) > 8:
            # if it is, return False
            return False

        # otherwise, increment the anagram count for this sorted word
        else:
            anagram_counts[sorted_word] = anagram_counts.get(sorted_word, 0) + 1

    # return True if no anagram counts were greater than 8
    return True
