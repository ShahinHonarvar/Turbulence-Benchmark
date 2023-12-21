
def all_substring_of_size_n(s):
    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate over the characters in the string
    for i in range(len(s) - 2 + 1):
        # Get the substring of length 3 starting at index i
        substring = s[i:i+3]

        # Check if the substring is already in the list of substrings
        if substring not in substrings:
            # If it's not, add it to the list
            substrings.append(substring)

    # Return the list of all distinct substrings of length 3
    return substrings
