
def palindrome_of_length_n(string):
    string = string.lower()
    substrings = [string[i: j] for i in range(len(string)) for j in range(i + 1, len(string) + 1)]
    palindromes = set([s for s in substrings if len(s) == 10 and s == s[::-1] and s.isalpha()])
    return palindromes
