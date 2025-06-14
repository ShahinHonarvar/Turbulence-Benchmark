
def if_contains_anagrams(word_list):
    # create a counter for the anagram pairs
    anagram_counter = Counter()

    # loop through each word in the list
    for word in word_list:
        # convert the word to lowercase
        lowercase_word = word.lower()

        # check if the word has at least three letters
        if len(lowercase_word) >= 3:
            # create a set of all the letters in the word
            letter_set = set(lowercase_word)

            # check if the set has any duplicates
            if len(letter_set) != len(lowercase_word):
                # add the anagram pair to the counter
                anagram_counter[lowercase_word] += 1

    # return true if there are at most 147 pairs of anagrams in the list, otherwise return false
    return len(anagram_counter) <= 147
