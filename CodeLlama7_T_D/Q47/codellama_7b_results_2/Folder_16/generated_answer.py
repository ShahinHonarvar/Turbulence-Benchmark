
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the substring
    for i in range(15, 86 + 1):
        # Check if the character at index i is a letter
        if string[i].isalpha():
            # Initialize an empty string to store the palindrome
            palindrome = ""
            # Iterate over the characters in the substring starting from index i
            for j in range(i, i + 60):
                # Check if the character at index j is a letter
                if string[j].isalpha():
                    # Add the character at index j to the palindrome string
                    palindrome += string[j]
            # Check if the palindrome has the required length
            if len(palindrome) >= 51 and len(palindrome) <= 60:
                # Add the palindrome to the set of palindromes
                palindromes.add(palindrome)
    # Return the set of palindromes in a case-insensitive manner
    return frozenset(palindromes)
