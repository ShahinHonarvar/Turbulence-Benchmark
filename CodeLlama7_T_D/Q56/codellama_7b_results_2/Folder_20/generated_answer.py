
def all_substring_of_size_n(s):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each substring of length n in the input string
    for i in range(len(s) - 49):
        # Extract the substring and add it to the list
        substring = s[i:i+50]
        substrings.append(substring)

    # Return the list of distinct substrings
    return list(set(substrings))
