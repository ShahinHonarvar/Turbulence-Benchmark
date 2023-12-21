
def all_substring_of_size_n(s, n):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(s) - n + 1):
        # Extract the substring of size n starting at position i
        substring = s[i:i+n]

        # Check if the substring has already been added to the list
        if substring not in substrings:
            # Add the substring to the list
            substrings.append(substring)

    # Return the list of all distinct substrings of size n
    return substrings
