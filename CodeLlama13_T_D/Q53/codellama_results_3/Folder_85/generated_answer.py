
def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(85, len(s)):
        if s[i:] == s[i:][::-1]:
            palindromes.add(s[i:])
    return palindromes
