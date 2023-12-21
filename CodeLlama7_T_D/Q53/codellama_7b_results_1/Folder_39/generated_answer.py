
def palindrome_of_length_at_least_n(string, n):
    # Define a function to check if a string is a palindrome
    def is_palindrome(s):
        return s == s[::-1]
    # Create a set to store all palindromes of length greater than or equal to n
    palindromes = set()
    # Iterate over each word in the string
    for word in string.split():
        # Check if the word is a palindrome and its length is greater than or equal to n
        if is_palindrome(word) and len(word) >= n:
            # Add the palindrome to the set
            palindromes.add(word)
    return palindromes
