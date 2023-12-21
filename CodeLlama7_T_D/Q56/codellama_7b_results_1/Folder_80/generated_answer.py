
def all_substring_of_size_n(s):
    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate over the characters of the string
    for i in range(len(s) - 29 + 1):
        # Extract a substring of length 30 starting from index i
        substring = s[i:i+30]

        # If the substring is not already in the list, add it to the list
        if substring not in substrings:
            substrings.append(substring)

    # Return the list of substrings
    return substrings
