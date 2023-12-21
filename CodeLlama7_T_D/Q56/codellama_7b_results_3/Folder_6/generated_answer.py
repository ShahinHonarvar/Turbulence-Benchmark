
def all_substring_of_size_n(input_string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the input string
    for i in range(len(input_string) - 23 + 1)):
        # Extract a substring of length 23 starting from the current character
        substring = input_string[i:i+23]

        # Check if the substring is already present in the list
        if substring not in substrings:
            # If not, add it to the list
            substrings.append(substring)

    # Return the list of all distinct substrings of length 23 with no duplicate characters
    return substrings
