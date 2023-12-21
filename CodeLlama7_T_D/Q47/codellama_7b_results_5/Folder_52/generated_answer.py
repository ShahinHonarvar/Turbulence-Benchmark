
def palindromes_of_specific_lengths(string, index_range=44, length_range=(13, 42)):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the substring
    for i in range(*index_range):
        # Check if the current character is a letter (a-zA-Z)
        if string[i].isalpha():
            # Initialize an empty string to store the palindrome
            palindrome = ""
            # Loop through each character in the substring from index i to index i + length_range - 1
            for j in range(i, i + *length_range):
                # Check if the current character is a letter (a-zA-Z)
                if string[j].isalpha():
                    # Add the current character to the palindrome
                    palindrome += string[j]
            # Check if the palindrome is found in a case-insensitive manner
            if palindrome.lower() == palindrome.lower().rstrip(palindrome[-1])[::-1].lower():
                # Add the palindrome to the set of palindromes
                palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
