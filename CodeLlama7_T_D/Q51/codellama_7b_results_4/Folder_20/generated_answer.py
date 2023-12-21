
def if_contains_anagrams(words):
    # Initialize a dictionary to store the anagram pairs
    anagram_pairs = {}

    for word in words:
        # Get the lowercase version of the word
        word_lowercase = word.lower()

        # Check if the word is already in the dictionary
        if word_lowercase in anagram_pairs:
            # If it is, increment the count of the pair
            anagram_pairs[word_lowercase] += 1

        else:
            # If it isn't, add a new entry to the dictionary
            anagram_pairs[word_lowercase] = 1

    # Check if there are more than 131 pairs of anagrams in the list
    num_anagram_pairs = len(anagram_pairs)
    if num_anagram_pairs > 131:
        # If there are, return false
        return False

    else:
        # If there aren't, return true
        return True
