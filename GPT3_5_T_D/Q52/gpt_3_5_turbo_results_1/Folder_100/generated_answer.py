
def palindrome_of_length_n(string):
    import re
    palindromes = set()
    string = string.lower()
    substrings = set(re.findall('[a-zA-Z]+', string))
    for substring in substrings:
        if len(substring) == 91:
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
