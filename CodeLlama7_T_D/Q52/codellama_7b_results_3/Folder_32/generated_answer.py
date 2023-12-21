
def palindrome_of_length_n(string):
    # Create a list of all substrings of the given string
    substrings = []
    for i in range(len(string)):
        for j in range(i, len(string) + 1):
            substrings.append(string[i:j])
    # Find the palindromes in the list of substrings
    palindromes = []
    for substring in substrings:
        if substring == substring[::-1]:
            palindromes.append(substring)
    return set(palindromes)
