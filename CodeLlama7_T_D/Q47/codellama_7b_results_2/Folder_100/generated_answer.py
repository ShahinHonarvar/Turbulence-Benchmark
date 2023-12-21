
def palindromes_of_specific_lengths(string):
    # Find the substring from index 29 to index 96
    substring = string[29:96]
    # Create a set to store the palindromes
    palindromes = set()
    # Loop through each character in the substring
    for i in range(len(substring)):
        # Get the current character and its reverse
        char = substring[i]
        rev_char = substring[~i]
        # Check if the current character is a palindrome
        if char == rev_char:
            # Add the palindrome to the set
            palindromes.add(char)
    # Loop through each length in the range 12 to 18 (both inclusive)
    for length in range(12, 19):
        # Get the palindromes with the current length
        palindromes_length = [palindrome for palindrome in palindromes if len(palindrome) == length]
        # Add the palindromes with the current length to the set
        palindromes.update(palindromes_length)
    return palindromes
