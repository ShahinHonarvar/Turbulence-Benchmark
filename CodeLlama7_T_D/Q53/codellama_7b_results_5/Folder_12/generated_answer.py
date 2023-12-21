
def palindrome_of_length_at_least_n(string, n):
    # Create a list of all words in the string
    words = string.split()
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each word in the string
    for word in words:
        # Check if the word is a palindrome of length greater than or equal to n
        if len(word) >= n and word == word[::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(word)
    return palindromes
