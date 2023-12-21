
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the character is a letter (not a digit or symbol)
        if string[i].isalpha():
            # Get the reverse of the substring starting at index i and ending at index len(string) - 1
            rev_substring = string[i:len(string)][::-1]
            # Check if the reversed substring is a palindrome
            if rev_substring == string[i:len(string)]:
                # Add the palindrome to the set
                palindromes.add(rev_substring)
    # Return the set of all palindromes of length greater than or equal to n that exist in the given string
    return palindromes
