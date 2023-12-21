
def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    length = 28
    for i in range(len(string) - length + 1):
        substr = string[i:i+length]
        if substr[::-1] == substr and substr.isalpha():
            palindromes.add(substr)
    return palindromes
