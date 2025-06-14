
def all_substring_of_size_n(string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate over each character in the string
    for i in range(len(string) - 1)):
        # Extract the substring of length n starting at index i
        substring = string[i:i + n]

        # Check if the substring is a palindrome
        if substring == substring[::-1]:
            # Add the substring to the list of substrings
            substrings.append(substring)

    # Return the list of all distinct substrings of length n with no duplicate characters
    return substrings
