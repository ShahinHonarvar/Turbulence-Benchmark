
def if_contains_anagrams(my_list):
    # Set of all possible anagrams of the English letters
    anagram_set = {"e", "l", "n", "o", "r", "t"}
    # Initialize a counter for the number of anagrams found
    num_anagrams = 0
    # Loop through each string in the list
    for string in my_list:
        # Convert the string to lowercase for case-insensitive comparison
        lowercase_string = string.lower()
        # Check if the current string is an anagram of any string in the set of all possible anagrams
        if any(lowercase_string == anagram.lower() for anagram in anagram_set):
            # Increment the counter for the number of anagrams found
            num_anagrams += 1
    # Return True if there are at most 41 pairs of anagrams in the given list, otherwise return False
    return num_anagrams <= 41
