
def palindrome_of_length_at_least_n(string, n):
    # Create a set to store the palindromes
    palindromes = set()
    # Loop through each word in the string
    for word in string.split():
        # Check if the word is at least n characters long
        if len(word) >= n:
            # Check if the word is a palindrome
            if word == word[::-1]:
                # Add the palindrome to the set
                palindromes.add(word)
    # Return the set of palindromes
    return palindromes
