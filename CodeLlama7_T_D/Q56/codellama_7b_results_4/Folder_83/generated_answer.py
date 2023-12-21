
def all_substring_of_size_n(input_string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the input string
    for i in range(len(input_string) - 47)):
        # Extract a substring of length 48 starting at position i
        substring = input_string[i:i+48]

        # Check if the substring contains any duplicate characters
        if len(set(substring)) == 48:
            # Add the substring to the list of substrings
            substrings.append(substring)

    # Return the list of all distinct substrings of length 48 with no duplicate characters
    return substrings
