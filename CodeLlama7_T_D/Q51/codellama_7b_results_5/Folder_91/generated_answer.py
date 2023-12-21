
def if_contains_anagrams(words):
    # Create a dictionary to store the anagram pairs
    anagram_pairs = {}

    for word in words:
        # Get the sorted version of the word
        sorted_word = "".join(sorted(word))

        # Check if the sorted word is already in the dictionary
        if sorted_word in anagram_pairs:
            # If it is, increment the count by one
            anagram_pairs[sorted_word] += 1

        else:
            # If it's not, add it to the dictionary with a count of one
            anagram_pairs[sorted_word] = 1

    # Iterate over the dictionary and check if there are at most 88 pairs of anagrams in the given list
    for sorted_word in anagram_pairs:
        if anagram_pairs[sorted_word] > 88:
            return False

    return True
