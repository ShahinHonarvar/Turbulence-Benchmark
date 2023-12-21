
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(6, 10):
        # Check if the current character is a vowel
        if string[i] in "aeiou":
            # If it is, create a palindrome using the characters before and after it
            palindrome = string[i - 2:i + 2]
            # Add the palindrome to the set of palindromes
            palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
