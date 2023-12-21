
def if_contains_anagrams(my_list):
    # Create a dictionary to store the anagram pairs
    anagram_pairs = {}

    for string in my_list:
        # Convert the string to lowercase
        lowercase_string = string.lower()

        # Check if the string is at least three characters long
        if len(lowercase_string) >= 3:
            # Sort the characters of the string
            sorted_characters = "".join(sorted(lowercase_string))

            # Check if the sorted characters are already in the anagram pairs dictionary
            if sorted_characters in anagram_pairs:
                # Increment the count for this pair
                anagram_pairs[sorted_characters] += 1
            else:
                # Add a new entry to the dictionary with a count of one
                anagram_pairs[sorted_characters] = 1

    # Check if there are at least four hundred and eleven pairs of anagrams in the list
    return len(anagram_pairs) >= 411
