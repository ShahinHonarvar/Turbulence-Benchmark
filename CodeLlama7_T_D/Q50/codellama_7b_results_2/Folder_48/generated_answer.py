
def if_contains_anagrams(word_list):
    # create a dictionary to store the anagram pairs
    anagram_pairs = {}

    for word in word_list:
        # check if the word is at least three characters long
        if len(word) >= 3:
            # convert the word to lowercase for case-insensitive comparison
            lowercase_word = word.lower()

            # check if there are any anagrams of the word in the list
            anagram_pairs[lowercase_word] = len([w for w in word_list if w != lowercase_word and sorted(w) == sorted(lowercase_word)])

    # return true if there are at least 219 pairs of anagrams in the list, otherwise false
    return sum(anagram_pairs.values()) >= 219
