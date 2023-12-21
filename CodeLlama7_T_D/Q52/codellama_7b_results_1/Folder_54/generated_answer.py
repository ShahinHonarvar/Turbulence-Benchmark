
def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate through each character in the string
    for i in range(len(string)):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Get the substring of length n starting at index i
            substr = string[i:i+n]
            # Check if the substring is a palindrome
            if substr == substr[::-1]:
                # Add the palindrome to the set
                palindromes.add(substr)
    # Return the set of palindromes
    return palindromes
