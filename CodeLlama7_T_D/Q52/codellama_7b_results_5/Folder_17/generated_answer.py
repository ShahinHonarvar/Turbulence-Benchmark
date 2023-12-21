
def palindrome_of_length_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each substring of length n in the input string
    for i in range(len(string) - n + 1):
        # Check if the current substring is a palindrome
        if string[i:i+n] == string[i:i+n][::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(string[i:i+n])
    # Return the set of palindromes
    return palindromes
