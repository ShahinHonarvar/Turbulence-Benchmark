
def palindrome_of_length_n(string, n):
    # Check if the input string is a palindrome of length n
    if len(string) < n:
        return set()
    else:
        # Initialize an empty set to store the palindromes
        palindromes = set()
        # Loop through each substring of length n in the input string
        for i in range(len(string) - n + 1):
            # Check if the current substring is a palindrome
            if string[i:i+n] == string[i:i+n][::-1]:
                # Add the palindrome to the set
                palindromes.add(string[i:i+n])
        return palindromes
