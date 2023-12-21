
def palindrome_of_length_at_least_n(string):
    # Split the string into a list of words
    words = string.split()
    
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Iterate over each word in the list
    for word in words:
        # Check if the current word is a palindrome
        if len(word) >= 48 and word == word[::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(word)
    
    # Return the set of palindromes
    return palindromes
