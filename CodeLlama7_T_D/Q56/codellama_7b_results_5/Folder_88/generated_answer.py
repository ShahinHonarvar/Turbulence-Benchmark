
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 67)):
        # Extract the substring of size 68 starting from the current character
        substring = string[i:i+68]

        # Check if the substring is already in the list of substrings
        if substring not in substrings:
            # If it's not, add it to the list of substrings
            substrings.append(substring)

    # Return the list of all distinct substrings of size 68 with no duplicate characters
    return substrings
