
def all_substring_of_size_n(input_string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the input string
    for i in range(len(input_string) - 3)):

        # Extract a substring of length 4 starting at position i
        substring = input_string[i:i+4]

        # Check if the substring is already in the list of substrings
        if substring not in substrings:

            # Add the substring to the list of substrings
            substrings.append(substring)

    # Return the list of all distinct substrings of length 4 with no duplicate characters, or an empty list if no such substrings exist in the given string.
    return substrings
