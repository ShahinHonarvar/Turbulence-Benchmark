
def palindrome_of_length_n(string, n):
    # convert the string to lowercase for case-insensitive comparison
    string = string.lower()

    # create a list of all substrings with length equal to 'n'
    substrings = [string[i:i+n] for i in range(len(string)-n+1)]

    # filter the substrings that are not palindromes
    palindromes = [substring for substring in substrings if substring == substring[::-1]]

    return set(palindromes)
