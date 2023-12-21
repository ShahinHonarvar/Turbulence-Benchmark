
def all_substring_of_size_n(string, n):
    # Check if the string is empty
    if len(string) == 0:
        return []

    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate over the characters in the string
    for i in range(len(string)):

        # Check if the substring is of size n
        if len(string[i:]) == n:

            # Add the substring to the list of substrings
            substrings.append(string[i:i + n])

    # Return the list of substrings
    return substrings
