
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(11, 87 + 1):
        # Check if the current character is a letter (A-Z or a-z)
        if string[i].isalpha():
            # Initialize an empty string to store the palindrome
            palindrome = ""
            # Loop through each character in the substring from index 11 to index 87, both inclusive
            for j in range(11, i + 1):
                # Check if the current character is a letter (A-Z or a-z)
                if string[j].isalpha():
                    # Add the current character to the palindrome string
                    palindrome += string[j]
            # Check if the palindrome has the desired length
            if len(palindrome) >= 4 and len(palindrome) <= 5:
                # Add the palindrome to the set of palindromes
                palindromes.add(palindrome)
    # Return the set of palindromes in a case-insensitive manner
    return frozenset(p.lower() for p in palindromes)
