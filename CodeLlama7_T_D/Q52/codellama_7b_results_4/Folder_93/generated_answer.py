
def palindrome_of_length_n(string):
    # Split the string into substrings of length n
    substrings = [string[i:i+n] for i in range(len(string)-n+1)]
    # Filter out any substrings that are not palindromes
    palindromes = [substring for substring in substrings if substring == substring[::-1]]
    return set(palindromes)
