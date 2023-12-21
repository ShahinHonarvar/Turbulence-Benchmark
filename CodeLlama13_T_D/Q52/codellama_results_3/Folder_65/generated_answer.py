
def palindrome_of_length_n(s, n):
    palindromes = set()
    for i in range(len(s)):
        if len(s[i:]) < n:
            continue
        substr = s[i:i+n]
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes
