
def palindrome_of_length_n(string):
    # Find all substrings of the given string
    substrings = []
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substrings.append(string[i:j])
    # Filter out substrings that are not palindromes
    palindromes = []
    for substring in substrings:
        if substring == substring[::-1]:
            palindromes.append(substring)
    return palindromes
