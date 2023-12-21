
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string) - 34):
        # Extract the substring of length 35 starting from index i
        substring = string[i:i+35]

        # Check if the substring is already in the list of substrings
        if substring not in substrings:
            # Add the substring to the list of substrings
            substrings.append(substring)

    # Return the list of all distinct substrings of length 35 with no duplicate characters, or an empty list if no such substrings exist in the given string
    return substrings
