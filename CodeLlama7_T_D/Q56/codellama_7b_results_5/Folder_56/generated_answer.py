
def all_substring_of_size_n(input_string):
    # Initialize an empty list to store the substrings
    substrings = []

    # Loop through each character in the input string
    for i in range(len(input_string) - 59)):

        # Extract the current substring of length 69
        substring = input_string[i:i+69]

        # Check if the substring is a palindrome
        if substring == substring[::-1]:

            # Add the palindromic substring to the list
            substrings.append(substring)

    # Return the list of all distinct substrings of length 69
    return substrings
