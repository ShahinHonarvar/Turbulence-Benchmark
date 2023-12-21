
def all_substring_of_size_n(string, n):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - n + 1):

        # Extract the substring of length n starting from the current index
        substring = string[i:i+n]

        # If the substring is not already in the list, add it
        if substring not in substrings:
            substrings.append(substring)

    # Return the list of all distinct substrings of length n
    return substrings
