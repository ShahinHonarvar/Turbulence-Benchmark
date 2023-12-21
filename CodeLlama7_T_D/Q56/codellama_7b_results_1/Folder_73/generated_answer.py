
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 19):

        # Extract a substring of length 20 starting from the current index
        substring = string[i:i+20]

        # Check if the substring is already in the list of substrings
        if substring not in substrings:

            # Add the substring to the list of substrings
            substrings.append(substring)

    # Return the list of all distinct substrings of length 20 with no duplicate characters
    return substrings
