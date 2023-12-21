
def if_contains_anagrams(words):
    # Create a set of all possible anagrams of the English letters
    all_anagrams = set()
    for word in words:
        # Get the sorted version of the word
        sorted_word = ''.join(sorted(word))
        # If the sorted word is not already in the set, add it
        if sorted_word not in all_anagrams:
            all_anagrams.add(sorted_word)
    # Return True if there are at most 50 pairs of anagrams in the given list
    return len(all_anagrams) <= 50
