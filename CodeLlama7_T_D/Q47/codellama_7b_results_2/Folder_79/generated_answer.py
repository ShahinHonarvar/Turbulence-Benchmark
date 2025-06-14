
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the string
    for i in range(1, len(string) - 8 + 1):
        # Extract a substring of length 9 from the current position
        substr = string[i:i+9]
        # Check if the substring is a palindrome
        if substr == substr[::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(substr)
    # Return the set of palindromes that meet the specified requirements
    return palindromes
