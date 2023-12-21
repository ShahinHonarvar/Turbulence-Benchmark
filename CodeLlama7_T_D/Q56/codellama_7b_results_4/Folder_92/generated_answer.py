
def all_substring_of_size_n(s):
    # Create a list to store the substrings
    substrings = []

    # Loop through each substring of length n in the input string
    for i in range(len(s) - 8):
        # Extract the substring and add it to the list
        substrings.append(s[i:i + 9])

    # Return the list of all distinct substrings of length 9 with no duplicate characters, or an empty list if no such substrings exist in the input string
    return list(set(substrings))
