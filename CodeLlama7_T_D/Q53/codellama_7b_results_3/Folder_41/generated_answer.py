 def palindrome_of_length_at_least_n(string, n=28):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each word in the string
    for word in string.split():
        # Check if the word is at least 28 characters long
        if len(word) >= n:
            # Check if the word is a palindrome
            if word == word[::-1]:
                # Add the word to the set of palindromes
                palindromes.add(word)
    # Return the set of palindromes
    return palindromes
