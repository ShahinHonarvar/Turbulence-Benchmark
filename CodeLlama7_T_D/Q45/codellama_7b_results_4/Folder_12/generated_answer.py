
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible arrangement of the English letters in the given string that occur between index 3 to index 8, both inclusive
    for i in range(3, 9):
        # Form a palindrome using the current arrangement of letters
        palindrome = ''.join([string[j] for j in range(i - 1, i + 2)])
        # Check if the palindrome has at least 4 characters and is case-insensitive
        if len(palindrome) >= 4 and palindrome.lower() == palindrome:
            # Add the palindrome to the set of palindromes
            palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
