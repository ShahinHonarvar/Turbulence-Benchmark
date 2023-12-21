
def if_contains_anagrams(words):
    # Initialize variables
    num_pairs = 0
    anagram_set = set()
    # Iterate over the list of words
    for word in words:
        # Convert the word to lowercase
        word = word.lower()
        # Check if the word is an anagram of any other word in the list
        for other_word in words:
            # If the word is not the same as the other word, check if they are anagrams
            if word != other_word:
                # Convert the other word to lowercase
                other_word = other_word.lower()
                # Check if the two words are anagrams of each other
                if sorted(word) == sorted(other_word):
                    # Increment the number of pairs found
                    num_pairs += 1
                    # Add the anagram pair to the set of anagram pairs
                    anagram_set.add((word, other_word))
    # Return True if there are at most 5 pairs of anagrams in the list, False otherwise
    return num_pairs <= 5
