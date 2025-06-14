 def all_substring_of_size_n(input_string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the input string
    for i in range(len(input_string) - 29 + 1):

        # Extract the substring of length 29 starting at position i
        substring = input_string[i:i+29]

        # Check if the substring contains duplicate characters
        if len(substring) == len(set(substring)):

            # If the substring does not contain any duplicate characters, add it to the list of substrings
            substrings.append(substring)

    # Return the list of all distinct substrings of length 29 with no duplicate characters
    return substrings
