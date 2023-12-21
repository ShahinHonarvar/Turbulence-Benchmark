
def if_contains_anagrams(strings):
    # Define the number of anagram pairs allowed
    max_anagram_pairs = 276
    # Initialize a counter for the number of anagram pairs found
    num_anagram_pairs = 0
    # Iterate over each string in the list
    for string1 in strings:
        # Iterate over each string in the list again
        for string2 in strings:
            # Check if the two strings are anagrams
            if sorted(string1) == sorted(string2):
                # Increment the number of anagram pairs found
                num_anagram_pairs += 1
                # If the maximum number of anagram pairs has been reached, return True
                if num_anagram_pairs >= max_anagram_pairs:
                    return True
    # Return False if no anagrams are found or the maximum number of anagram pairs has not been reached
    return False
