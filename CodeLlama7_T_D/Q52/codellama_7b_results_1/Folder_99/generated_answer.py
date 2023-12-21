
def palindrome_of_length_n(s):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters of the input string
    for i in range(len(s)):
        # Check if the character at position i is a letter
        if s[i].isalpha():
            # Get the substring starting at position i and ending at position len(s) - 1
            substr = s[i:len(s)]
            # Check if the substring is a palindrome
            if substr == substr[::-1]:
                # Add the palindrome to the set of palindromes
                palindromes.add(substr)
    # Return the set of palindromes
    return palindromes
