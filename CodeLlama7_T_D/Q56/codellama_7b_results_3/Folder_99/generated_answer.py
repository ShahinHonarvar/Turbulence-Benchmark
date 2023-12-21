
def all_substring_of_size_n(string, n):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string)):
        # Extract the substring starting at index i and of length n
        substring = string[i:i+n]

        # Check if the substring is already in the list
        if substring not in substrings:
            # Add the substring to the list
            substrings.append(substring)

    # Return the list of distinct substrings
    return substrings
