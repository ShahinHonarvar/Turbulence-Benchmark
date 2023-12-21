 def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(1, 10):
        # Get the current character and its lowercase equivalent
        char = string[i]
        lower_char = char.lower()
        # Check if the current character is a letter or not
        if char.isalpha():
            # If the current character is a letter, add it to the palindrome
            palindrome = lower_char + lower_char[::-1]
            # Add the palindrome to the set of palindromes
            palindromes.add(palindrome)
    return palindromes
