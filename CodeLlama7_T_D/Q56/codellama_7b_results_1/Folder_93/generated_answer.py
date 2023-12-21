
def all_substring_of_size_n(string, n):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - n + 1):

        # Extract a substring of length n from the string starting at position i
        substring = string[i:i+n]

        # If the substring is not already in the list of substrings, add it to the list
        if substring not in substrings:
            substrings.append(substring)

    # Return the list of all distinct substrings of length n
    return substrings
