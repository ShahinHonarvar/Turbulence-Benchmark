
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible length of a palindrome
    for i in range(6, len(string) + 1):
        # Get all substrings of the specified length
        substrings = [string[j:j + i] for j in range(len(string) - i + 1))]
        # Check if any of the substrings is a palindrome
        for substring in substrings:
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
