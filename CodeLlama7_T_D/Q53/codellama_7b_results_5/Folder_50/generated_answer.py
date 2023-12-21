
def palindrome_of_length_at_least_n(s, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each substring of length greater than or equal to n in the input string
    for i in range(len(s) - n + 1):
        # Extract the current substring
        substr = s[i:i+n]
        # Check if the substring is a palindrome in a case-insensitive manner
        if substr == substr[::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(substr)
    # Return the set of palindromes
    return palindromes
