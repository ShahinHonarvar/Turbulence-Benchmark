
def palindrome_of_length_n(string):
    # Split the string into substrings of length n
    substrings = [string[i:i+n] for i in range(len(string)-n+1)]
    # Filter out substrings that are not palindromes
    palindromes = [s for s in substrings if s == s[::-1]]
    return set(palindromes)
