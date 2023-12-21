 def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(11, 96 + 1):
        # Check if the current character is a letter (not whitespace or punctuation)
        if string[i].isalpha():
            # Initialize an empty string to store the palindrome
            palindrome = ""
            # Loop through each character in the substring starting from index i and ending at index 96, both inclusive
            for j in range(i, 96 + 1):
                # Check if the current character is a letter (not whitespace or punctuation)
                if string[j].isalpha():
                    # Append the current character to the palindrome string
                    palindrome += string[j]
            # Check if the palindrome string has the required length between 45 and 52 (both inclusive)
            if len(palindrome) >= 45 and len(palindrome) <= 52:
                # Add the palindrome to the set of palindromes
                palindromes.add(palindrome)
    # Return the set of palindromes in a case-insensitive manner
    return palindromes
