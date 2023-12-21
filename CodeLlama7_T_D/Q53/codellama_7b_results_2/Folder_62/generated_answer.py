
def palindrome_of_length_at_least_n(string, n=31):
    # Create a list of all words in the string
    words = string.split()

    # Initialize an empty set to store the palindromes

    palindromes = set()

    # Iterate over each word in the string

    for word in words:

        # Check if the word is a palindrome

        if word == word[::-1]:

            # Add the word to the set of palindromes

            palindromes.add(word)

    # Return the set of palindromes

    return palindromes
