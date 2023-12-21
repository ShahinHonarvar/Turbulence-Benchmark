
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each word in the string
    for word in string.split():
        # Check if the word is a palindrome and has a length greater than or equal to 55
        if word == word[::-1] and len(word) >= n:
            # Add the palindrome to the set
            palindromes.add(word)
    # Return the set of palindromes
    return palindromes
