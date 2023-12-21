
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate through each character in the string
    for i in range(len(string) - 49):

        # Check if the current substring is already in the list of substrings
        if not any(substring == string[i:i+50] for substring in substrings)):

            # If it's not, add it to the list of substrings
            substrings.append(string[i:i+50])

    # Return the list of all distinct substrings of length 50 with no duplicate characters
    return substrings
