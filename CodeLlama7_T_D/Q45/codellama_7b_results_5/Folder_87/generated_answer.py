
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(3, 9 + 1):
        # Create a substring of length 3 starting at index i
        substr = string[i - 3:i]
        # Check if the substring is a palindrome
        if substr == substr[::-1]:
            # Add the substring to the set of palindromes
            palindromes.add(substr)
    # Return the set of palindromes
    return palindromes
