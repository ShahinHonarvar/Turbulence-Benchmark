
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the substring starting from the current index and ending at the end of the string
        substr = string[i:]
        # Loop through each character in the reversed substring
        for j in range(len(substr)-1, -1, -1):
            # Check if the character is a letter (A-Z or a-z)
            if substr[j].isalpha():
                # Get the palindrome by concatenating the current character and the reversed substring
                palindrome = substr[j] + substr[:j]
                # Add the palindrome to the set
                palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
