
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string)):
        # Get the current character and the next 46 characters
        char = string[i]
        next_chars = string[i + 1:i + 47]
        # Check if the next 46 characters contain the same character as the current character
        if next_chars.count(char) == 46:
            # Add the substring to the list of substrings
            substrings.append(string[i:i + 47])

    return substrings
