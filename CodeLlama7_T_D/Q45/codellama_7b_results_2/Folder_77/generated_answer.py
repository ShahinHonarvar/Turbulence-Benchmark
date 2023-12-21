
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the possible combinations of letters in the specified range
    for i in range(4, len(string) - 2):
        # Generate a palindrome by reversing the order of the letters in the current combination
        palindrome = string[i:i+2]
        # Check if the generated palindrome has a length of at least 4 and is case-insensitively equal to itself
        if len(palindrome) >= 4 and palindrome.lower() == palindrome:
            # Add the generated palindrome to the set of palindromes
            palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
