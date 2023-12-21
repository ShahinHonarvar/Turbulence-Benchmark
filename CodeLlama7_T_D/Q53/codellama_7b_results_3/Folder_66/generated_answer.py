
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the character is a letter (not a whitespace or punctuation)
        if string[i].isalpha():
            # Create a substring of length at least n starting from the current index
            substr = string[max(0, i - n + 1):i + 1]
            # Check if the substring is a palindrome (has the same characters in reverse order)
            if substr == substr[::-1]:
                # Add the palindrome to the set
                palindromes.add(substr)
    # Return the set of palindromes found in the string
    return palindromes
