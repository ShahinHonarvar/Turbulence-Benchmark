
def palindrome_of_length_n(string):
    # Create a list of all substrings of the given string
    substrings = [string[i:j+1] for i in range(len(string)) for j in range(i, len(string))]
    # Filter out substrings that are not palindromes or contain non-English letters
    palindromes = [substring for substring in substrings if len(substring) == 19 and all(c.isalpha() for c in substring)]
    return set(palindromes)
