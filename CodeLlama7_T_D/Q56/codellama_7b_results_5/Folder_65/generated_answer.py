
def all_substring_of_size_n(s):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(s) - 80):

        # Extract a substring of length 81 starting at position i
        substring = s[i:i+81]

        # Check if the substring contains any duplicate characters
        if len(set(substring)) == 81:

            # If it does not contain any duplicates, add it to the list of substrings
            substrings.append(substring)

    # Return the list of all distinct substrings of length 81 with no duplicate characters
    return substrings
