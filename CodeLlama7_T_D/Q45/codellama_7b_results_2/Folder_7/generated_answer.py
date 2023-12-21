
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop over all possible pairs of indices in the string
    for i in range(1, len(string) - 1):
        for j in range(i + 1, len(string)):
            # Check if the substring starting at index i and ending at index j is a palindrome
            substring = string[i:j]
            if substring == substring[::-1]:
                # Add the palindrome to the set
                palindromes.add(substring)
    return palindromes
