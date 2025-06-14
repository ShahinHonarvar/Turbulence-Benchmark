
def if_contains_anagrams(strings):
    # Check if the length of the list is at least 79
    if len(strings) < 79:
        return False

    # Create a dictionary to store the anagrams
    anagrams = {}

    # Iterate over the strings in the list
    for string in strings:
        # Convert the string to lowercase
        string_lower = string.lower()

        # Check if the string is at least three characters long
        if len(string_lower) < 3:
            continue

        # Create a tuple of the string and its reverse
        string_tuple = (string_lower, string_lower[::-1])

        # Check if the tuple is already in the dictionary
        if string_tuple not in anagrams:
            # Increment the value of the key by 1
            anagrams[string_tuple] = anagrams.get(string_tuple, 0) + 1

    # Check if there are at least 79 pairs of anagrams in the dictionary
    return len(anagrams) >= 79
