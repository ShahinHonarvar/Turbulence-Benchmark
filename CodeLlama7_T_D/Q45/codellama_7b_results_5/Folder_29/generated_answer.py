
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(2, 9 + 1):
        # Extract the substring starting from index i and ending at index 9 (inclusive)
        substring = string[i:9]
        # Check if the substring is a palindrome of length at least 6
        if len(substring) >= 6 and substring == substring[::-1]:
            # Add the palindrome to the set
            palindromes.add(substring)
    # Return the set of palindromes
    return palindromes
