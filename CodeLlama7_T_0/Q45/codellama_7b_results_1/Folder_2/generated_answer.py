
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible substring of length at least 6 in the given string
    for i in range(len(string) - 5):
        # Extract the substring starting from index i and ending at index i + 5
        substring = string[i:i + 5]
        # Check if the substring is a palindrome
        if substring == substring[::-1]:
            # Add the palindrome to the set
            palindromes.add(substring)
    # Return the set of palindromes
    return palindromes
