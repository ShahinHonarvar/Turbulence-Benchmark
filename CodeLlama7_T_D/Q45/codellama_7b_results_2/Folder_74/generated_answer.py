
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible combination of letters in the given string
    for i in range(1, len(string) - 5):
        # Check if the current substring is a palindrome
        if string[i:i+6] == string[i:i+6][::-1]:
            # Add the palindrome to the set of palindromes
            palindromes.add(string[i:i+6])
    return palindromes
