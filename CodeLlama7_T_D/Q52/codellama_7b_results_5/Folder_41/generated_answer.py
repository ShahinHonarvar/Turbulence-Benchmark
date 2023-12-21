
def palindrome_of_length_n(string):
    # Find all substrings of length n in the given string
    substrings = [string[i:i+n] for i in range(len(string)-n+1)]
    # Filter out substrings that are not case-insensitive palindromes
    palindromes = [s for s in substrings if s == s[::-1]]
    return set(palindromes)
