
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Get the reverse of the substring starting at index i and ending at the end of the string
            rev_substring = string[i:][::-1]
            # Check if the reverse of the substring is a palindrome
            if rev_substring == string[i:]:
                # Add the palindrome to the set
                palindromes.add(string[i:])
    # Return the set of palindromes
    return palindromes
