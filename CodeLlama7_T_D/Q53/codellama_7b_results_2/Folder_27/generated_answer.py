
def palindrome_of_length_at_least_n(string, n):
    # Define a function to check if a string is a palindrome or not
    def is_palindrome(s):
        return s == s[::-1]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the input string
    for i in range(len(string)):
        # Check if the character is a letter (uppercase or lowercase)
        if string[i].isalpha():
            # Convert the character to uppercase
            uppercase_char = string[i].upper()
            # Check if the converted character is a palindrome
            if is_palindrome(uppercase_char):
                # Add the palindrome to the set
                palindromes.add(uppercase_char)
    # Return the set of palindromes
    return palindromes
