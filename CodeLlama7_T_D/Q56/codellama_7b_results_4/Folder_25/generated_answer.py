
def all_substring_of_size_n(string, n):
    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate over the length of the string
    for i in range(len(string) - n + 1):
        # Extract the substring of size n starting at index i
        substring = string[i:i+n]

        # Check if the substring is already in the list of substrings
        if substring not in substrings:
            # Add the substring to the list of substrings
            substrings.append(substring)

    # Return the list of all distinct substrings of size n
    return substrings
