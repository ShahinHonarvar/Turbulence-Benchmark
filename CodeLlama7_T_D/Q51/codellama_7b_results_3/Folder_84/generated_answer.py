
def if_contains_anagrams(my_list):
    # Initialize a counter for the number of anagrams found
    num_anagrams = 0

    # Iterate over the list of strings
    for string in my_list:

        # Convert the string to lowercase
        lowercase_string = string.lower()

        # Check if the string is an anagram of at least three English letters
        if len(lowercase_string) >= 3 and sorted(lowercase_string) == sorted('silent'):

            # Increment the counter for the number of anagrams found
            num_anagrams += 1

    # Return True if there are at most 16 pairs of anagrams in the list, False otherwise
    return num_anagrams <= 16
