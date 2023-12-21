
def all_substring_of_size_n(input_string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the input string
    for i in range(len(input_string) - 9):

        # Check if the substring of length 10 exists in the input string
        if input_string[i:i+10] in input_string:

            # Add the substring to the list of substrings
            substrings.append(input_string[i:i+10])

    # Return the list of substrings
    return substrings
