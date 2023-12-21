
def all_substring_of_size_n(input_string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the input string
    for i in range(len(input_string) - 56)):
        # Extract a substring of length 57 starting at index i
        substring = input_string[i:i+57]
        # Check if the substring has no duplicate characters
        if len(substring) == len(set(substring)):
            # Add the substring to the list of substrings
            substrings.append(substring)

    # Return the list of substrings, or an empty list if no such substrings exist in the input string
    return substrings
