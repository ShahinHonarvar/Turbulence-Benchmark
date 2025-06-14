
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each substring of the given string that is at least 4 characters long
    for i in range(len(string) - 3):
        # Check if the current substring is a palindrome
        if string[i:i+4] == string[i:i+4][::-1]:
            # Add the current palindrome to the set of palindromes
            palindromes.add(string[i:i+4])
    return palindromes
