
def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each substring of the input string
    for i in range(len(string) - 463):
        # Check if the current substring is a palindrome
        if string[i:i+464] == string[i:i+464][::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(string[i:i+464])
    return palindromes
