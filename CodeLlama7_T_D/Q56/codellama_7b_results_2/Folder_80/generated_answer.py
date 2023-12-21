
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 29):

        # Extract the substring of length 31 starting at index i
        substring = string[i:i+31]

        # Check if the substring is already in the list
        if substring not in substrings:

            # If it's not, add it to the list
            substrings.append(substring)

    # Return the list of all distinct substrings of length 31
    return substrings
