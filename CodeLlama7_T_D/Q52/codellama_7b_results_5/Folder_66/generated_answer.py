
def palindrome_of_length_n(string):
    # Find all substrings of length n in the string
    substrings = [string[i:i+n] for i in range(len(string)-n+1)]
    # Filter out non-palindromes and case-sensitive palindromes
    palindromes = [s for s in substrings if s == s[::-1] and not any(c.islower() for c in s)]
    return set(palindromes)
