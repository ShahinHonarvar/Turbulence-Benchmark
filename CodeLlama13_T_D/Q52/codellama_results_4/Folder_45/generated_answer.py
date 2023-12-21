
def palindrome_of_length_n(string):
    # find all substrings of length 21 in the given string
    substrings = [string[i:i+21] for i in range(len(string)-20)]
    
    # filter out non-palindromes using a regular expression
    palindromes = [s for s in substrings if re.match("^[a-zA-Z]{21}$", s) and s == s[::-1]]
    
    return set(palindromes)
