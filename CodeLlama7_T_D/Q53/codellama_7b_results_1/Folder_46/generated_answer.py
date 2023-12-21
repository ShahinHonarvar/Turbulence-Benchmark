
def palindrome_of_length_at_least_n(string, n):
    # Define a set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the character is uppercase or lowercase
        if string[i].isupper() or string[i].islower():
            # Define a variable to store the palindrome
            palindrome = ""
            # Loop through each character in the string starting from the current index and ending at the end of the string
            for j in range(i, len(string)):
                # Check if the current character is uppercase or lowercase
                if string[j].isupper() or string[j].islower():
                    # Add the current character to the palindrome variable
                    palindrome += string[j]
            # Check if the palindrome has a length greater than or equal to 86
            if len(palindrome) >= n:
                # Add the palindrome to the set of palindromes
                palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
