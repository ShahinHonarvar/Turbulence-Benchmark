
def palindrome_of_length_at_least_n(string):
    # Split the string into a list of words
    words = string.split()
    
    # Create an empty set to store the palindromes
    palindromes = set()
    
    # Iterate over each word in the list
    for word in words:
        # Check if the word is a palindrome
        if word == word[::-1]:
            # Add the word to the palindromes set
            palindromes.add(word)
    
    return palindromes
