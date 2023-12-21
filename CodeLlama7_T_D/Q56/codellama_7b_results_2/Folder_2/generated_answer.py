
def all_substring_of_size_n(input_string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate over each character in the input string
    for i in range(len(input_string) - 56 + 1)):
        # Extract a substring of length 56 from the current position
        substring = input_string[i:i+56]

        # If the substring is not empty and does not contain any duplicate characters, add it to the list of substrings
        if len(substring) == 56 and len(set(substring)) == 56:
            substrings.append(substring)

    # Return the list of all distinct substrings of length 56 with no duplicate characters
    return substrings
