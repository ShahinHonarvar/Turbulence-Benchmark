
def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Get the substring of the string starting from the current character and with length equal to 4
            substr = string[i:i+4]
            # Check if the substring is a palindrome
            if substr == substr[::-1]:
                # Add the palindrome to the set of palindromes
                palindromes.add(substr)
    # Return the set of palindromes found in the string
    return palindromes
