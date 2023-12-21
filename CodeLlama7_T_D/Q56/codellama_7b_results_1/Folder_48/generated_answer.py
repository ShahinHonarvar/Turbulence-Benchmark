
def all_substring_of_size_n(input_string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the input string
    for i in range(len(input_string) - 120 + 1):

        # Extract a substring of length 120 starting at position i
        substring = input_string[i:i+120]

        # Check if the substring has no duplicate characters
        if len(substring) == len(set(substring)):

            # Add the substring to the list of substrings
            substrings.append(substring)

    # Return the list of substrings
    return substrings
