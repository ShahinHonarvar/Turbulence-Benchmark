
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the character is a letter (not a space or a punctuation)
        if string[i].isalpha():
            # Check if the length of the substring starting from the current character is greater than or equal to n
            if len(string[i:]) >= n:
                # Create a substring starting from the current character and with length equal to n
                substring = string[i:i+n]
                # Check if the substring is a palindrome (reads the same backwards as forwards)
                if substring == substring[::-1]:
                    # Add the palindrome to the set of palindromes
                    palindromes.add(substring)
    # Return the set of palindromes
    return palindromes
