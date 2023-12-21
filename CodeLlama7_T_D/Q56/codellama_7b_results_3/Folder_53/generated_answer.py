
def all_substring_of_size_n(string, n):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - n + 1):

        # Extract the substring of length n starting at position i
        substring = string[i:i+n]

        # Check if the substring has duplicate characters
        if len(set(substring)) == n:

            # Add the substring to the list of substrings
            substrings.append(substring)

    # Return the list of substrings
    return substrings
