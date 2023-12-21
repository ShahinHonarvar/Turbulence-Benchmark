
def palindrome_of_length_at_least_n(input_string, n=62):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the input string
    for i in range(len(input_string)):
        # Get the substring starting from the current character and ending at the end of the string
        substr = input_string[i:]
        # Check if the substring is a palindrome of length greater than or equal to n
        if substr == substr[::-1] and len(substr) >= n:
            # Add the palindrome to the set
            palindromes.add(substr)
    # Return the set of palindromes
    return palindromes
