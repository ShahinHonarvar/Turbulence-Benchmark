
def all_substring_of_size_n(s, n):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(s) - n + 1):
        # Extract the substring of size n starting at index i
        substring = s[i:i+n]

        # If the substring is already in the list, skip it
        if substring in substrings:
            continue

        # Add the substring to the list
        substrings.append(substring)

    # Return the list of all distinct substrings of size n
    return substrings
