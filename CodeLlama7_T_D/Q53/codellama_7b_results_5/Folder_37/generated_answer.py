
def palindrome_of_length_at_least_n(s, n):
    # Create a set to store the palindromes
    palindromes = set()
    # Iterate over each word in the string
    for word in s.split():
        # Check if the word is at least n characters long
        if len(word) >= n:
            # Check if the word is a palindrome
            if word == word[::-1]:
                # Add the palindrome to the set
                palindromes.add(word)
    # Return the set of palindromes
    return palindromes
