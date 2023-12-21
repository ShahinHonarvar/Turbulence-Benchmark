
def palindrome_of_length_n(string):
    length = 87
    palindromes = set()
    for i in range(len(string) - length + 1):
        substr = string[i:i+length]
        if substr.lower() == substr.lower()[::-1] and substr.isalpha():
            palindromes.add(substr)
    return palindromes
