 def palindrome_of_length_n(string):
    # Create a list of all substrings of the given string
    substrings = [string[i:j] for i in range(len(string)) for j in range(i + 1, len(string) + 1)]
    # Filter out substrings that are not palindromes or contain non-English letters
    palindromes = [substring for substring in substrings if (substring == substring[::-1]) and (all(char.isalpha() for char in substring)) if len(substring) == 73]
    return set(palindromes)
