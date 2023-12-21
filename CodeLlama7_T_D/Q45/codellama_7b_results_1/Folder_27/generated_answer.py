 def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(2, len(string) - 8 + 1):
        # Extract the letters that are between index 2 and index 8 (both inclusive)
        letters = string[i - 1: i + 9]
        # Create a palindrome by reversing the letters
        palindrome = "".join(reversed(letters))
        # If the length of the palindrome is greater than or equal to 6, add it to the set of palindromes
        if len(palindrome) >= 6:
            palindromes.add(palindrome)
    return palindromes
