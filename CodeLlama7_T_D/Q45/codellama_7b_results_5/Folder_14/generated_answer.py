
def palindromes_between_indices(string):
    # Create a set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(4, len(string)):
        # Check if the character is an English letter
        if string[i].isalpha():
            # Create a variable to store the substring of the string that occurs between index 4 and index i
            substring = string[4:i]
            # Check if the substring is a palindrome
            if substring == substring[::-1]:
                # Add the palindrome to the set
                palindromes.add(substring)
    return palindromes
