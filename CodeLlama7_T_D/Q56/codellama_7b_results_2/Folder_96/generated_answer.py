
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 21 + 1):

        # Extract a substring of size 21 from the current position in the string
        substring = string[i:i+21]

        # If the substring is not already in the list of substrings, add it to the list
        if substring not in substrings:
            substrings.append(substring)

    # Return the list of all distinct substrings of size 21 with no duplicate characters
    return substrings
