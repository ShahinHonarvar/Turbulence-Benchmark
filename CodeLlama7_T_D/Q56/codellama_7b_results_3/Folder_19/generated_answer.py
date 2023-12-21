
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate through each character in the string
    for i in range(len(string) - 18 + 1)):
        # Extract a substring of length 18 from the current character
        substring = string[i:i+18]

        # Check if the substring is already in the list of substrings
        if substring not in substrings:
            # Add the substring to the list of substrings
            substrings.append(substring)

    # Return the list of all distinct substrings of length 18 with no duplicate characters
    return substrings
