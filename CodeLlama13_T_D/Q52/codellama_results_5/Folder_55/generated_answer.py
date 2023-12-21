
def palindrome_of_length_n(string):
    # Find all substrings of the given string that are 97 characters long
    substrings = [string[i:i+97] for i in range(len(string)-97)]
    
    # Filter out non-palindromes by checking if each substring is a palindrome
    palindromes = [substring for substring in substrings if substring == substring[::-1]]
    
    return set(palindromes)
