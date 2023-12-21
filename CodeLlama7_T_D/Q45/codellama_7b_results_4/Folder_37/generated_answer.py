
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each substring of length 5 in the string
    for i in range(len(string) - 4 + 1):
        # Extract the substring and check if it is a palindrome
        substring = string[i:i+5]
        if substring == substring[::-1]:
            # Add the palindrome to the set
            palindromes.add(substring)
    return palindromes
