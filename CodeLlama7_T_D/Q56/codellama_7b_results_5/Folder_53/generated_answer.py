
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 25 + 1):
        # Extract a substring of size 25 from the current position
        substring = string[i:i+25]

        # Check if the substring contains any duplicate characters
        if len(substring) == len(set(substring)):
            # If it does not contain any duplicate characters, add it to the list of substrings
            substrings.append(substring)

    # Return the list of all distinct substrings of size 25 with no duplicate characters
    return substrings
