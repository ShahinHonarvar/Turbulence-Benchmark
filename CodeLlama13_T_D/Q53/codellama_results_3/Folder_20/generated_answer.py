
def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(len(s) - 5):
        if s[i:i+6] == s[i:i+6][::-1]:
            palindromes.add(s[i:i+6])
    return palindromes
