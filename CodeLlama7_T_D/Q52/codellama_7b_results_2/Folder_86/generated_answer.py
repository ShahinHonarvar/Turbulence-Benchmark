
def palindrome_of_length_n(string):
    # Create a list of all substrings of the given string
    substrings = [string[i:j+1] for i in range(len(string)) for j in range(i, len(string))]
    # Filter out any substrings that are not palindromes
    palindromes = [substring for substring in substrings if substring == substring[::-1]]
    # Return the set of all palindromes of length n
    return set(palindromes)
