
def palindromes_of_specific_lengths(string):
    # Define the substring range
    start = 10
    end = 59
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the substring
    for i in range(start, end + 1):
        # Check if the character is a letter (not a whitespace or a punctuation)
        if string[i].isalpha():
            # Define the palindrome with the current character
            palindrome = string[i]
            # Iterate over the characters in the substring from the current index to the end of the substring
            for j in range(i + 1, end + 1):
                # Check if the character is a letter (not a whitespace or a punctuation)
                if string[j].isalpha():
                    # Add the character to the palindrome
                    palindrome += string[j]
            # Check if the palindrome has the required length
            if len(palindrome) >= 18 and len(palindrome) <= 36:
                # Add the palindrome to the set of palindromes
                palindromes.add(palindrome)
    # Return the set of palindromes in a case-insensitive manner
    return frozenset(palindromes)
