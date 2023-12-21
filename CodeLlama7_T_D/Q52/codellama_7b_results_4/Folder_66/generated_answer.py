
def palindrome_of_length_n(string):
    # Remove all non-alphabetical characters from the string
    string = ''.join([c for c in string if c.isalpha()])
    # Create a list of all substrings of length n
    substrings = [string[i:i+n] for i in range(len(string)-n+1)]
    # Filter the substrings to only include palindromes
    palindromes = [s for s in substrings if s == s[::-1]]
    return set(palindromes)
