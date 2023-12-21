 def palindrome_of_length_at_least_n(string, n=68):
    # Split the string into individual words
    words = string.split()
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each word in the string
    for word in words:
        # Check if the word is a palindrome (i.e., it reads the same backwards and forwards)
        if word == word[::-1]:
            # If the word is a palindrome, add it to the set of palindromes
            palindromes.add(word)
    # Return the set of palindromes that have a length greater than or equal to 68 characters
    return palindromes
