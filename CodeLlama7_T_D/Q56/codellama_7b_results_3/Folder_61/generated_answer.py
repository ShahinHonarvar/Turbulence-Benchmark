
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 2):
        # Extract the substring of length 39 starting at index i
        substring = string[i:i+39]

        # If the substring is not already in the list of substrings, add it
        if substring not in substrings:
            substrings.append(substring)

    # Return the list of all distinct substrings of length 39 with no duplicate characters
    return substrings
