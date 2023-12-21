
def if_contains_anagrams(word_list):
    # create a dictionary to store the anagram pairs
    anagram_pairs = {}
    for word in word_list:
        # convert the word to lowercase
        word = word.lower()
        # sort the letters of the word
        sorted_letters = "".join(sorted(word))
        # check if there is a pair of anagrams in the dictionary
        if sorted_letters in anagram_pairs:
            # increment the count of the pair
            anagram_pairs[sorted_letters] += 1
        else:
            # add the new pair to the dictionary
            anagram_pairs[sorted_letters] = 1
    # check if there are more than 206 pairs of anagrams in the dictionary
    if len(anagram_pairs) > 206:
        return False
    else:
        return True
