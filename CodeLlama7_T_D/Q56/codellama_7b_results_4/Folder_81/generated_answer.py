
def all_substring_of_size_n(input_string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate through each character in the input string
    for i in range(len(input_string) - 89)):
        # Extract a substring of length 98 from the current position
        substring = input_string[i:i+98]

        # Check if the extracted substring contains duplicate characters
        if len(substring) == len(set(substring)):
            # If no duplicate characters exist, add the substring to the list of substrings
            substrings.append(substring)

    # Return the list of all distinct substrings of length 98 with no duplicate characters
    return substrings
