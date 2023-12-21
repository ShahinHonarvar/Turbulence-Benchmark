
def all_substring_of_size_n(string, n):
    # Check if the string is empty or has less than n characters
    if len(string) < n:
        return []

    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate through each substring of length n in the given string
    for i in range(len(string) - n + 1):

        # Check if the current substring has any duplicate characters
        if len(set(string[i:i+n])) == n:

            # Add the current substring to the list of substrings
            substrings.append(string[i:i+n])

    # Return the list of all distinct substrings of length n with no duplicate characters
    return substrings
