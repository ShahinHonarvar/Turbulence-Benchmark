
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each letter in the string
    for i in range(7, 10):
        # Check if the letter is a vowel
        if string[i].lower() in ["a", "e", "i", "o", "u"]:
            # If it is a vowel, create a palindrome using the vowel and the two letters on either side of it
            palindrome = string[i - 1] + string[i].lower() + string[i + 1]
            # Add the palindrome to the set of palindromes
            palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
