
def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the string
    for i in range(len(string)):
        # Check if the character is a letter
        if string[i].isalpha():
            # Create a substring of length n starting at index i
            substring = string[i:i+n]
            # Check if the substring is a palindrome
            if substring == substring[::-1]:
                # Add the palindrome to the set
                palindromes.add(substring)
    # Return the set of palindromes
    return palindromes
