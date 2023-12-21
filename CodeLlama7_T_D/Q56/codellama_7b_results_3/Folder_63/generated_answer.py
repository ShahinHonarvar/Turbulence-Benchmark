
def all_substring_of_size_n(string, n):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - n + 1):

        # Extract the substring of length n starting at position i
        substring = string[i:i+n]

        # Add the substring to the list if it is not already present
        if substring not in substrings:
            substrings.append(substring)

    # Return the list of all distinct substrings of length n
    return substrings
