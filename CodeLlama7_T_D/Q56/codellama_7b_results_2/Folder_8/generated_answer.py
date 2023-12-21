
def all_substring_of_size_n(s):
    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate over each character in the string
    for i in range(len(s)):
        # Extract the substring starting at position i and of length n
        substring = s[i:i+n]

        # If the substring is not already in the list, add it to the list
        if substring not in substrings:
            substrings.append(substring)

    # Return the list of all distinct substrings of length n
    return substrings
