
def palindrome_of_length_n(string):
    # Find all substrings of length n in the given string
    substrs = [string[i:i+n] for i in range(len(string)-n+1)]
    # Filter out non-palindromes and return the set of palindromes
    return {s for s in substrs if s == s[::-1]}
