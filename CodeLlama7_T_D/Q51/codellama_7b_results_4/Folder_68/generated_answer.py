
def if_contains_anagrams(words):
    # Create a dictionary to store the anagram pairs
    anagram_pairs = {}

    for word in words:
        # Check if the word is at least three letters long
        if len(word) >= 3:
            # Convert the word to lowercase
            word = word.lower()

            # Check if there are any anagrams of the word in the list
            for other_word in words:
                # Make sure we're not comparing a word with itself
                if word != other_word:
                    # Convert the other_word to lowercase
                    other_word = other_word.lower()
                    # Check if the two words are anagrams of each other
                    if sorted(word) == sorted(other_word):
                        # Add the pair to the dictionary
                        if (word, other_word) in anagram_pairs:
                            anagram_pairs[(word, other_word)] += 1
                        else:
                            anagram_pairs[(word, other_word)] = 1
    # Check if there are more than 94 pairs of anagrams in the list
    if len(anagram_pairs) > 94:
        return False

    else:

        return True
