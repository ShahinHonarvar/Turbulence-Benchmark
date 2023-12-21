
def palindrome_of_length_n(s):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each substring of length n in the input string
    for i in range(len(s) - 29 + 1):
        # Check if the current substring is a palindrome
        if s[i:i+29] == s[i:i+29][::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(s[i:i+29])
    # Return the set of palindromes
    return palindromes
