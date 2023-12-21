
def all_substring_of_size_n(s):
    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate over the characters in the string
    for i in range(len(s)):
        # Get the substring starting at index i and of length n
        substring = s[i:i+n]

        # If the substring is not already in the list, add it to the list
        if substring not in substrings:
            substrings.append(substring)

    # Return the list of substrings
    return substrings
