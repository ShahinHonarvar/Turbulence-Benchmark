
def palindrome_of_length_n(string):
    palindromes = set()
    length = 223
    string = string.lower()
    for i in range(len(string) - length + 1):
        substr = string[i:i+length]
        if substr == substr[::-1] and substr.isalpha():
            palindromes.add(substr)
    return palindromes
