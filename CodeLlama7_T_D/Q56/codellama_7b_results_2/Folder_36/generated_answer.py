 def all_substring_of_size_n(input_string):
    # Initialize an empty list to store the substrings
    substrings = []
    # Loop through each character in the input string
    for i in range(len(input_string) - 145)):
        # Extract a substring of length 146 starting at position i
        substring = input_string[i:i+146]
        # Check if the substring contains any duplicate characters
        if len(set(substring)) == len(substring):
            # If the substring is unique, add it to the list of substrings
            substrings.append(substring)
    # Return the list of all distinct substrings of length 146 with no duplicate characters
    return substrings
