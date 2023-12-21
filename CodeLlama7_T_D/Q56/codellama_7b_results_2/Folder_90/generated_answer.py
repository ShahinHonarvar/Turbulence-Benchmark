
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string)):

        # Extract the substring starting from index i and of length 130
        substring = string[i:i+130]

        # If the substring is not empty and does not contain any duplicate characters, add it to the list of substrings
        if substring != "" and len(substring) == 130 and len(set(substring)) == 130:
            substrings.append(substring)

    # Return the list of all distinct substrings of length 130 with no duplicate characters, or an empty list if no such substrings exist in the given string
    return substrings
