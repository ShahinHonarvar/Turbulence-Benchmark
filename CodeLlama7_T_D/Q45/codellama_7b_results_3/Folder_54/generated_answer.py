
def palindromes_between_indices(s):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each substring of length 4 or more in s
    for i in range(len(s) - 3):
        # Extract the substring
        sub = s[i:i+4]
        # Check if the substring is a palindrome
        if sub == sub[::-1]:
            # Add the palindrome to the set
            palindromes.add(sub)
    # Return the set of palindromes
    return palindromes
