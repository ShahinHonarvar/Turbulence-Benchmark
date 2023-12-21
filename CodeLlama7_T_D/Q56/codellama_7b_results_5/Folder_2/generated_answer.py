
def all_substring_of_size_n(s):
    n = 56
    # Create a list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(s) - n + 1):
        # Extract the substring of size n starting at position i
        substring = s[i:i+n]

        # Check if the substring has any duplicate characters
        if len(substring) == len(set(substring)):
            # If it doesn't have any duplicates, add it to the list of substrings
            substrings.append(substring)

    # Return the list of substrings
    return substrings
