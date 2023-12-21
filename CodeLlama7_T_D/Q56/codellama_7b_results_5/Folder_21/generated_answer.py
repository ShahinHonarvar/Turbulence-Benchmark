
def all_substring_of_size_n(input_string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate over the length of the input string
    for i in range(len(input_string) - 106 + 1):

        # Extract a substring of length 106 from the input string starting at index i
        substring = input_string[i:i+106]

        # If the substring is not already in the list of substrings, add it to the list
        if substring not in substrings:
            substrings.append(substring)

    # Return the list of substrings
    return substrings
