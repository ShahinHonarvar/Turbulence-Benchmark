
def palindrome_of_length_n(string, n):
    # Create a list of all substrings of length n in the given string
    substrings = [string[i:i+n] for i in range(len(string)-n+1)]
    # Filter out non-palindromes and return the set of palindromes
    return {s for s in substrings if s == s[::-1]}
