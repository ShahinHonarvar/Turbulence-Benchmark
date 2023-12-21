
def if_contains_anagrams(list_of_strings):
    # Create a dictionary to store the anagram pairs
    anagram_pairs = {}

    # Loop through each string in the list
    for string in list_of_strings:

        # Convert the string to lowercase
        lowercase_string = string.lower()

        # Check if there are at least 3 characters in the string
        if len(lowercase_string) >= 3:

            # Sort the characters of the string
            sorted_characters = ''.join(sorted(lowercase_string))

            # Check if the sorted characters have already been added to the anagram pairs dictionary
            if sorted_characters not in anagram_pairs:

                # Add the sorted characters and their anagrams to the anagram pairs dictionary
                anagram_pairs[sorted_characters] = [string, ''.join(reversed(sorted_characters)))]

    # Return True if there are at least 93 pairs of anagrams in the given list, and False otherwise
    return len(anagram_pairs) >= 93
