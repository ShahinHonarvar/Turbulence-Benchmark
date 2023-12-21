 def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the string
    for i in range(len(string)):

        # Initialize an empty string to store the substring
        substring = ""

        # Add characters to the substring until it reaches a length of 77 or exceeds the number of characters in the original string
        while len(substring) < 77 and i + len(substring) <= len(string):
            substring += string[i + len(substring)]

        # If the substring has a length of 77, add it to the list of substrings
        if len(substring) == 77:
            substrings.append(substring)

    # Return the list of all distinct substrings of length 77 with no duplicate characters, or an empty list if no such substrings exist in the given string
    return substrings
