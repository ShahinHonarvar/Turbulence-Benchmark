
def all_substring_of_size_n(string, n):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - n + 1):

        # Extract the substring of length n starting at index i
        substring = string[i:i+n]

        # Check if the substring is already in the list
        if substring not in substrings:

            # If it's not, add it to the list
            substrings.append(substring)

    # Return the list of all distinct substrings of length n
    return substrings
