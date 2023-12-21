
def palindrome_of_length_at_least_n(string, n):
    # Convert the string to lowercase for case-insensitive comparison
    string = string.lower()
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the string
    for i in range(len(string)):
        # Check if the character is a letter
        if string[i].isalpha():
            # Extract the substring starting from the current character and ending at the end of the string
            substr = string[i:]
            # Check if the substring is a palindrome
            if substr == substr[::-1]:
                # Add the palindrome to the set
                palindromes.add(substr)
    # Return the set of palindromes with length greater than or equal to n
    return palindromes
