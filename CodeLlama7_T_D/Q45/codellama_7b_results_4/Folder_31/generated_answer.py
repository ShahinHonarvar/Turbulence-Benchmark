
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each index in the range of [1, 8]
    for i in range(1, 9):
        # Create a substring of length 6 starting from index i
        substring = string[i:i+6]
        # Check if the substring is a palindrome in a case-insensitive manner
        if substring == substring[::-1]:
            # Add the palindrome to the set
            palindromes.add(substring)
    # Return the set of palindromes
    return palindromes
