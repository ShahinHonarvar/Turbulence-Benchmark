
def palindrome_of_length_n(string, n):
    # Find all substrings of length n in the given string
    substrings = [string[i:i+n] for i in range(len(string)-n+1)]
    # Return the set of all palindromes found
    return {substring for substring in substrings if substring == substring[::-1]}
