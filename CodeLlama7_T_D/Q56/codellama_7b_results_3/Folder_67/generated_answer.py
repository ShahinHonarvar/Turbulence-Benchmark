
def all_substring_of_size_n(input_string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the input string
    for i in range(len(input_string) - 42):
        # Extract a substring of length 43 starting at position i
        substring = input_string[i:i+43]

        # Check if the substring contains duplicate characters
        if len(set(substring)) == 43:
            # Add the substring to the list of substrings
            substrings.append(substring)

    # Return the list of all distinct substrings of length 43 with no duplicate characters
    return substrings
