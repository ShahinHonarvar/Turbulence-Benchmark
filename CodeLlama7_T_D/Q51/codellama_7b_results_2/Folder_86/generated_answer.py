
def if_contains_anagrams(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return False

    # Initialize a set to store anagram pairs
    anagram_pairs = set()

    # Iterate over the list of strings
    for string in my_list:
        # Convert the string to lowercase
        lowercase_string = string.lower()

        # Check if the string is at least three characters long
        if len(lowercase_string) >= 3:
            # Create a sorted list of the characters in the string
            sorted_characters = sorted(list(lowercase_string))

            # Check if the sorted list of characters is already in the set of anagram pairs
            if sorted_characters not in anagram_pairs:
                # Add the sorted list of characters to the set of anagram pairs
                anagram_pairs.add(sorted_characters)

    # Check if there are at most 48 pairs of anagrams in the given list
    return len(anagram_pairs) <= 48
