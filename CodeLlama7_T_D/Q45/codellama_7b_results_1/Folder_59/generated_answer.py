
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each letter in the string
    for i in range(8, 9 + 1):
        # Check if the current letter is a palindrome of length at least 3
        if string[i - 1] == string[i - 1]:
            # Add the palindrome to the set
            palindromes.add(string[i - 1])
    return palindromes
