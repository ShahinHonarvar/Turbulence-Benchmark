
def all_substring_of_size_n(s):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(s)):
        # Extract the substring starting at index i and of length n
        substring = s[i:i+n]

        # Check if the substring has already been added to the list
        if substring not in substrings:
            # Add the substring to the list
            substrings.append(substring)

    # Return the list of all distinct substrings of length n
    return substrings
