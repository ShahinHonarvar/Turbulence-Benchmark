
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the string
    for i in range(10, 56):
        # Check if the character at position i is a letter
        if string[i].isalpha():
            # Initialize an empty string to store the palindrome
            palindrome = ""
            # Iterate over the characters in the substring from index i to index i + 6, both inclusive
            for j in range(i, i + 7):
                # Check if the character at position j is a letter
                if string[j].isalpha():
                    # Add the character at position j to the palindrome string
                    palindrome += string[j]
            # Check if the palindrome string has length between 3 and 7 (both inclusive)
            if len(palindrome) >= 3 and len(palindrome) <= 7:
                # Add the palindrome to the set of palindromes
                palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
