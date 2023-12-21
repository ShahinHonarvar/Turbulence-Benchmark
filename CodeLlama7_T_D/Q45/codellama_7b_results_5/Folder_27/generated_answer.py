
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(2, 8 + 1):
        # Get the substring starting from index i and ending at index i + 1
        substr = string[i:i + 2]
        # Check if the substring is a palindrome
        if substr == substr[::-1]:
            # Add the palindrome to the set
            palindromes.add(substr)
    return palindromes
