
def all_substring_of_size_n(s, n):
    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate over the characters in the string
    for i in range(len(s) - n + 1):
        # Extract a substring of length n from the current position
        substring = s[i:i+n]

        # Check if the substring is already in the list of substrings
        if substring not in substrings:
            # If it's not, add it to the list
            substrings.append(substring)

    # Return the list of all distinct substrings of length n
    return substrings
