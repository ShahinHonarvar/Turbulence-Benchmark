
def if_contains_anagrams(my_list):
    # Create a dictionary to store the anagram pairs
    anagram_pairs = {}

    # Iterate over the list of strings
    for string in my_list:

        # Convert the string to lowercase
        lowercase_string = string.lower()

        # Sort the characters in the string
        sorted_characters = "".join(sorted(lowercase_string))

        # Check if the sorted string is already in the dictionary of anagram pairs
        if sorted_characters in anagram_pairs:

            # If it is, increment the count for that pair
            anagram_pairs[sorted_characters] += 1

        else:

            # If it's not, add a new entry to the dictionary with a count of one
            anagram_pairs[sorted_characters] = 1

    # Check if there are more than 52 pairs of anagrams in the list
    if len(anagram_pairs) > 52:

        # If there are, return false
        return False

    else:

        # If there aren't, return true
        return True
