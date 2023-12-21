
def palindrome_of_length_at_least_n(string, n):
    # Create a set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the character at index i
        char = string[i]
        # If the character is a letter...
        if char.isalpha():
            # ...loop through each character in the string backwards from index i...
            for j in range(len(string) - 1, i, -1):
                # ...if the current character is the same as the previous character...
                if char == string[j]:
                    # ...add the palindrome to the set of palindromes...
                    palindromes.add(string[i:j+1])
            # If no palindromes were found, add an empty string to the set of palindromes
            if not palindromes:
                palindromes.add('')
    # Return the set of palindromes
    return palindromes
