
def if_contains_anagrams(my_list):
    # Create a dictionary to store the anagram counts
    anagram_counts = {}

    # Iterate over the list and count the anagrams
    for word in my_list:
        # Get the letters of the word in a set
        letter_set = set(word.lower())

        # Check if there are at least three letters in the set
        if len(letter_set) >= 3:
            # Sort the letters in the set and make them a tuple
            sorted_letters = tuple(sorted(letter_set))

            # Increment the count for this anagram
            if sorted_letters in anagram_counts:
                anagram_counts[sorted_letters] += 1

            else:
                anagram_counts[sorted_letters] = 1

    # Check if there are at least 194 pairs of anagrams in the list
    return len(anagram_counts) >= 194
