
def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 365):
        substr = string[i:i+366]
        if substr.lower() == substr.lower()[::-1] and substr.isalpha():
            palindromes.add(substr)
    return palindromes
