
def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 92):
        substr = string[i:i+93]
        if substr == substr[::-1] and substr.isalpha():
            palindromes.add(substr)
    return palindromes
