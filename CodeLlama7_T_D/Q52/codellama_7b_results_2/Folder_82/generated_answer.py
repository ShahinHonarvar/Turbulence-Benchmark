
def palindrome_of_length_n(string):
    # Create a list of all substrings of length n in the given string
    substring_list = [string[i:i+n] for i in range(len(string)-n+1)]
    # Filter out any substrings that are not palindromes
    palindrome_list = [substring for substring in substring_list if substring == substring[::-1]]
    return set(palindrome_list)
