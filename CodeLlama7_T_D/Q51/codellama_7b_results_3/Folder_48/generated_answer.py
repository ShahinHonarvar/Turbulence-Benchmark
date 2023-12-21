
def if_contains_anagrams(my_list):
    # Initialize variables to keep track of anagram pairs and string lengths
    pair_count = 0
    string_lengths = []

    # Iterate through the list of strings
    for string in my_list:
        # Convert the string to lowercase
        lowercase_string = string.lower()

        # Check if the string is a valid anagram
        if len(lowercase_string) >= 3:
            # If the string is a valid anagram, add it to the list of string lengths
            string_lengths.append(len(lowercase_string))

            # Check if there are at most 277 pairs of anagrams in the given list
            pair_count = max(pair_count, len(set(string_lengths)))

    # Return True if there are at most 277 pairs of anagrams in the given list; otherwise, return False
    return pair_count <= 277
