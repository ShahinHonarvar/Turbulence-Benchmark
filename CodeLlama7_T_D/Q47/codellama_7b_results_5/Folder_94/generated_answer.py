 def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate through the substring from index 40 to index 94 (both inclusive)
    for i in range(40, 95):
        # Check if the character at index i is a letter
        if string[i].isalpha():
            # Initialize an empty string to store the palindrome
            palindrome = ""
            # Iterate through the characters from index i - 1 to index i + 1 (both inclusive)
            for j in range(i - 1, i + 2):
                # Check if the character at index j is a letter
                if string[j].isalpha():
                    # Add the character at index j to the palindrome string
                    palindrome += string[j]
            # Check if the length of the palindrome string is between 45 and 51 (both inclusive)
            if len(palindrome) >= 45 and len(palindrome) <= 51:
                # Add the palindrome to the set of palindromes
                palindromes.add(palindrome)
    # Return the set of palindromes in a case-insensitive manner
    return frozenset(palindromes)
