
def if_contains_anagrams(strings):
    # Initialize a counter for the number of anagrams found
    num_anagrams = 0
    # Iterate over each string in the list
    for string in strings:
        # Get the length of the string
        length = len(string)
        # Check if the length of the string is at least three
        if length >= 3:
            # Create a set of all the letters in the string
            letters = set(string.lower())
            # Check if there are any duplicates in the set of letters
            if len(letters) != length:
                # Increment the number of anagrams found
                num_anagrams += 1
    # Return True if there are at most eighty-one pairs of anagrams in the list, and False otherwise.
    return num_anagrams <= 81
