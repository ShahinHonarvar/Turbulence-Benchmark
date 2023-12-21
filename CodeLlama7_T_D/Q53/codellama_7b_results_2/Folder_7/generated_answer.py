
def palindrome_of_length_at_least_n(input_string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each word in the input string
    for word in input_string.split():
        # Check if the word is a palindrome of length greater than or equal to n
        if word == word[::-1] and len(word) >= n:
            # Add the palindrome to the set
            palindromes.add(word)
    # Return the set of palindromes
    return palindromes
