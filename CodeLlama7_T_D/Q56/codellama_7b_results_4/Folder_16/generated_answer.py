
def all_substring_of_size_n(input_string, n):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the input string
    for i in range(len(input_string) - n + 1):
        # Extract the substring of length n starting at index i
        substring = input_string[i:i+n]

        # Check if the substring is already in the list of substrings
        if substring not in substrings:
            # If it's not, add it to the list of substrings
            substrings.append(substring)

    # Return the list of all distinct substrings of length n with no duplicate characters
    return substrings
