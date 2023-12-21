
def palindrome_of_length_n(string, n):
    palindromes = set()
    for i in range(len(string)):
        substr = string[i:i+n]
        if len(substr) == n and substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes
