
def palindrome_of_length_at_least_n(string, n):
    # Create a set to store the palindromes
    palindromes = set()
    # Loop through each substring of length greater than or equal to 20 in the given string
    for i in range(len(string) - n + 1):
        # Check if the substring is a palindrome
        if string[i:i+n] == string[i:i+n][::-1]:
            # Add the palindrome to the set
            palindromes.add(string[i:i+n])
    # Return the set of palindromes
    return palindromes
