
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 14):
        # Extract a substring of length 15 starting at position i
        substring = string[i:i+15]

        # Check if the substring is already in the list
        if substring not in substrings:
            # Add the substring to the list
            substrings.append(substring)

    # Return the list of substrings
    return substrings
