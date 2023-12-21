
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate through each character in the string
    for i in range(len(string) - 94):

        # Extract a substring of length 95 starting from position i
        substring = string[i:i+95]

        # Check if the substring contains any duplicate characters
        if len(substring) == len(set(substring)):
            substrings.append(substring)

    # Return the list of all distinct substrings of length 95 with no duplicate characters
    return substrings
