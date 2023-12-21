
def all_substring_of_size_n(input_string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the input string
    for i in range(len(input_string) - 5 + 1)):
        # Extract the substring of length 6 starting at index i
        substring = input_string[i:i+6]

        # Check if the substring has no duplicate characters
        if len(set(substring)) == 6:
            # Add the substring to the list of substrings
            substrings.append(substring)

    # Return the list of substrings, or an empty list if none exist
    return substrings
