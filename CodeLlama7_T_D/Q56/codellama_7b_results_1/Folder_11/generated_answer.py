
def all_substring_of_size_n(input_string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate over the characters in the input string
    for i in range(len(input_string) - 78 + 1):
        # Extract a substring of length 78 from the input string
        substring = input_string[i:i+78]

        # Check if the substring contains any duplicate characters
        if len(substring) == len(set(substring)):
            # If it does not contain any duplicate characters, add it to the list of substrings
            substrings.append(substring)

    # Return the list of substrings
    return substrings
