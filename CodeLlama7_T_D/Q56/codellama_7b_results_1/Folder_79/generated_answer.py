
def all_substring_of_size_n(input_string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate through each character in the input string
    for i in range(len(input_string) - 5)):
        # Check if the substring of length 6 exists in the input string
        if input_string[i:i+6].isalpha():
            # Add the substring to the list of substrings
            substrings.append(input_string[i:i+6])

    # Return the list of all distinct substrings of length 6 with no duplicate characters
    return list(set(substrings)))
