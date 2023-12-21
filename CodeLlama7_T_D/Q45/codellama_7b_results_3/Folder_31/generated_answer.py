
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible combination of letters in the string
    for i in range(1, len(string) - 8 + 1):
        for j in range(i + 1, len(string) - 7 + 1):
            # Check if the substring is a palindrome
            substring = string[i:j]
            if substring == substring[::-1]:
                # Add the palindrome to the set
                palindromes.add(substring)
    return palindromes
