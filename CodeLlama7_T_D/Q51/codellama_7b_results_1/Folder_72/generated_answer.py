
def if_contains_anagrams(my_list):
    # Initialize variables for counting anagrams and length of strings
    num_anagrams = 0
    string_length = 0

    # Iterate through list, checking for anagrams and updating variables accordingly
    for string in my_list:
        # Count number of anagrams
        if is_anagram(string):
            num_anagrams += 1

        # Update length of strings
        string_length = max(string_length, len(string))

    # Check if there are at most 188 pairs of anagrams in the given list
    return num_anagrams <= 188 and string_length >= 3

# Function to check if a string is an anagram
def is_anagram(string):
    # Convert string to lowercase for case-insensitive comparison
    string = string.lower()

    # Check if string is a permutation of "qwerty"
    return sorted(string) == sorted("qwerty")
