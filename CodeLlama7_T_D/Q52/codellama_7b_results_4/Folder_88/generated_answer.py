
def palindrome_of_length_n(string):
    # Define a function to check if a string is a palindrome
    def is_palindrome(s):
        return s == s[::-1]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each substring of length n in the given string
    for i in range(len(string) - 13 + 1):
        # Check if the substring is a palindrome
        if is_palindrome(string[i:i+13]):
            # Add the palindrome to the set
            palindromes.add(string[i:i+13])
    return palindromes
