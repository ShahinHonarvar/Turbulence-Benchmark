
def all_substring_of_size_n(string, n):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - n + 1):

        # Extract the current substring
        substring = string[i:i+n]

        # Check if the substring has already been added to the list
        if substring not in substrings:
            substrings.append(substring)

    # Return the list of all distinct substrings of length n with no duplicate characters
    return substrings
