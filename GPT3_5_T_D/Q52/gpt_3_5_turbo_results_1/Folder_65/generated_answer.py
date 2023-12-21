
def palindrome_of_length_n(string):
    palindromes = set()
    n = 35
    string = string.lower()
    for i in range(len(string) - n + 1):
        substr = string[i:i+n]
        if substr == substr[::-1] and substr.isalpha():
            palindromes.add(substr)
    return palindromes
