
def all_substring_of_size_n(string, n):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - n + 1):

        # Extract the substring of length n starting from current index
        substring = string[i:i+n]

        # Check if the substring is already in the list
        if substring not in substrings:

            # Add the substring to the list
            substrings.append(substring)

    # Return the list of all distinct substrings of length n
    return substrings
