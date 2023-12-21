
def palindromes_between_indices(s):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each substring of length 4 or more in the input string
    for i in range(len(s) - 3):
        # Check if the substring is a palindrome
        if s[i:i+4] == s[i:i+4][::-1]:
            # Add the palindrome to the set of palindromes
            palindromes.add(s[i:i+4])
    return palindromes
