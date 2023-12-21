
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible arrangement of the English letters in the given string that occur between index 6 to index 9, both inclusive
    for i in range(6, 10):
        # Initialize an empty string to store the current palindrome
        current_palindrome = ""
        # Loop through each character of the string from index i to index 9, both inclusive
        for j in range(i, 10):
            # Add the character at index j to the current palindrome
            current_palindrome += string[j]
        # Check if the current palindrome has a length of at least 4 and is created from any possible arrangement of the English letters in the given string that occur between index 6 to index 9, both inclusive
        if len(current_palindrome) >= 4 and all([c.isalpha() for c in current_palindrome]):
            # Add the current palindrome to the set of palindromes
            palindromes.add(current_palindrome)
    return palindromes
