
def palindrome_of_length_at_least_n(input_string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the input string
    for i in range(len(input_string)):
        # Get the substring starting from the current character and extending to the end of the string
        substr = input_string[i:]
        # Check if the substring is a palindrome
        if substr == substr[::-1]:
            # Add the palindrome to the set
            palindromes.add(substr)
    # Return the set of palindromes
    return palindromes
