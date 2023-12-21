
def palindromes_of_specific_lengths(string, min_length=55, max_length=71):
    # Define a function to check if a string is a palindrome
    def is_palindrome(word):
        return word == word[::-1]

    # Create a list of all the words in the given string
    words = string.split()

    # Create an empty set to store the palindromes
    palindromes = set()

    # Iterate over each word and check if it is a palindrome
    for word in words:
        if is_palindrome(word) and min_length <= len(word) <= max_length:
            palindromes.add(word)

    # Return the set of all palindromes that meet the requirements
    return palindromes
