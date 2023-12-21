
def if_contains_anagrams(strings):
    # Check if the input is a list of strings
    if not all(isinstance(s, str) for s in strings)):
        raise ValueError("Input must be a list of strings")
    # Create a dictionary to store the number of anagrams for each length
    lengths = {}

    # Iterate over the input list and count the number of anagrams for each length
    for string in strings:
        # Convert the string to lowercase for case-insensitive comparison
        string = string.lower()

        # Check if the string is a palindrome
        if string == "".join(reversed(string)):
            # Get the length of the string
            length = len(string)

            # Increment the number of anagrams for the given length
            lengths[length] = lengths.get(length, 0) + 1

    # Check if there are at most 72 pairs of anagrams in the input list
    return all(num_anagrams <= 72 for num_anagrams in lengths.values())
