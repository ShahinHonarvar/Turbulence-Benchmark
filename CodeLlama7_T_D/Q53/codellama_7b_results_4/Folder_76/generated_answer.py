
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Create a substring of length at least n starting from the current character
            substr = string[i:i+n]
            # Check if the substring is a palindrome
            if substr == substr[::-1]:
                # Add the palindrome to the set
                palindromes.add(substr)
    return palindromes
