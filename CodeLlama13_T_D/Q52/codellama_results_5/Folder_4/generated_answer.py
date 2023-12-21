
def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s) - 14):
        substr = s[i:i+15]
        if len(substr) == 15 and substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes
