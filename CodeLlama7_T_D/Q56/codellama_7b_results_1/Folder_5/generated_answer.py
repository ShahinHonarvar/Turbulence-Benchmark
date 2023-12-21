
def all_substring_of_size_n(input_string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the input string
    for i in range(len(input_string) - 5)):

        # Check if the current substring is already in the list of substrings
        if input_string[i:i+6] not in substrings:
            # If it's not, add it to the list of substrings
            substrings.append(input_string[i:i+6])

    # Return the list of substrings
    return substrings
