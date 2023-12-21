
def palindrome_of_length_n(string):
    palindromes = set()
    string = string.lower()
    for i in range(len(string) - 16):
        substr = string[i:i+17]
        if substr == substr[::-1] and substr.isalpha():
            palindromes.add(substr)
    return palindromes
