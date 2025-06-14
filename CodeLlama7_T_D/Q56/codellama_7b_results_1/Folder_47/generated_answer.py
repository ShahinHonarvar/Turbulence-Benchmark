
def all_substring_of_size_n(input_string, n):
    # Check if the input string is valid
    if len(input_string) < n:
        return []

    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each possible starting index of a substring
    for i in range(len(input_string) - n + 1):

        # Extract the substring of length n starting at position i
        substring = input_string[i:i+n]

        # Check if the substring has duplicate characters
        if len(substring) == len(set(substring)):

            # If the substring is unique, add it to the list of substrings
            substrings.append(substring)

    # Return the list of all distinct substrings of length n with no duplicate characters
    return substrings
