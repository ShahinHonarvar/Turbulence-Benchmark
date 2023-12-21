 def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []
    # Loop through each character in the string
    for i in range(len(string) - 116):
        # Extract a substring of length 117 starting at index i
        substring = string[i:i+117]
        # Check if the substring has no duplicate characters
        if len(substring) == len(set(substring)):
            # Add the substring to the list of substrings
            substrings.append(substring)
    # Return the list of all distinct substrings of length 117 with no duplicate characters
    return substrings
