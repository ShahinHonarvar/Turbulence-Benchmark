
def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 72):
        substr = string[i:i+73]
        if substr.isalpha() and substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes
