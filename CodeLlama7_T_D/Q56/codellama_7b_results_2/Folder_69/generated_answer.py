
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate over the length of the string
    for i in range(len(string) - 89):

        # Extract the substring of length 99 from the current index
        substring = string[i:i+99]

        # Check if the substring contains any duplicate characters
        if len(substring) == len(set(substring)):

            # If the substring is valid, add it to the list of substrings
            substrings.append(substring)

    # Return the list of all distinct substrings of length 99 with no duplicate characters
    return substrings
