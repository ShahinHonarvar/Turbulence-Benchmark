
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible substring of length at least 3 in the given string
    for i in range(1, len(string) - 2):
        # Check if the substring is a palindrome
        if string[i] == string[i + 1]:
            # Add the palindrome to the set
            palindromes.add(string[i:i + 3])
    return palindromes
