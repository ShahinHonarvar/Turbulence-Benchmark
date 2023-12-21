
def palindromes_between_indices(s):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(4, 9 + 1):
        # Check if the current character is a letter
        if s[i].isalpha():
            # Convert the current character to lowercase
            c = s[i].lower()
            # Add the palindrome to the set
            palindromes.add(c + c)
    return palindromes
