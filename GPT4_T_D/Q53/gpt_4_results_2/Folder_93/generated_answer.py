
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            if len(substring) >= 90 and substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
