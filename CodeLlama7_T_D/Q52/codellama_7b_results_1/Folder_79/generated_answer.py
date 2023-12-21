
def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Create a substring of length 64 starting from the current character
            substring = string[i:i+64]
            # Check if the substring is a palindrome
            if substring == substring[::-1]:
                # Add the palindrome to the set
                palindromes.add(substring)
    # Return the set of palindromes
    return palindromes
