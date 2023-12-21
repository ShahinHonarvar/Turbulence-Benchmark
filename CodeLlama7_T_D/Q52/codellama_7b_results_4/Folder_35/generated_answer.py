
def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the string
    for i in range(len(string)):
        # Check if the character is a letter
        if string[i].isalpha():
            # Check if the substring starting at position i and ending at position len(string) - 1 is a palindrome
            if string[i:len(string)] == string[i:len(string)][::-1]:
                # Add the palindrome to the set of palindromes
                palindromes.add(string[i:len(string)])
    return palindromes
