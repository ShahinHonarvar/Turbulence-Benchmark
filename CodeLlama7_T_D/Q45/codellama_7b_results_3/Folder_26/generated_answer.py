
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(4, 6 + 1):
        # Get the current character and its reverse complement
        char = string[i]
        rev_comp = char.lower() if char.isupper() else char.upper()
        # Check if the current character is a vowel or a consonant
        if char in "aeiou" or rev_comp in "aeiou":
            # Add the palindrome to the set
            palindromes.add(char + rev_comp)
    return palindromes
