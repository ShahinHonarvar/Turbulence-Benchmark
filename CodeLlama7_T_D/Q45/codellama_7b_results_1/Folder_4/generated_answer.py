
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(3, 9 + 1):
        # Check if the current character is a vowel
        if string[i] in "aeiou":
            # Create a palindrome by reversing the characters on both sides of the current character
            palindrome = string[:i] + string[i+1:]
            # Add the palindrome to the set
            palindromes.add(palindrome)
    return palindromes
