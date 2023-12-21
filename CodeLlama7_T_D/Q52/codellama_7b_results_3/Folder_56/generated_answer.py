
def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the character is a letter (i.e., not a space or punctuation)
        if string[i].isalpha():
            # Check if the substring starting at index i and ending at index len(string) - 1 is a palindrome
            if string[i:len(string)] == string[i:len(string)] [::-1]:
                # Add the palindrome to the set of palindromes
                palindromes.add(string[i:len(string)])
    # Return the set of palindromes
    return palindromes
