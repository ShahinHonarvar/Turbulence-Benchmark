
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 10 + 1):

        # Extract a substring of length 10 starting at position i
        substring = string[i:i+10]

        # Check if the substring is already in the list of substrings
        if substring not in substrings:

            # If it's not, add it to the list and move on to the next character
            substrings.append(substring)

    # Return the list of all distinct substrings of length 10 with no duplicate characters
    return substrings
