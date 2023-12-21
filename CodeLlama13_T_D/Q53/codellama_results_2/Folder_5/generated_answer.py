
def palindrome_of_length_at_least_n(string, n):
    palindromes = set()
    for i in range(len(string) - n + 1):
        substr = string[i:i+n]
        if len(substr) >= 46 and substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes
