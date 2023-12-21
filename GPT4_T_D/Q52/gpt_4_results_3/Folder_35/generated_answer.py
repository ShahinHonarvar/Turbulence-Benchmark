
def palindrome_of_length_n(s):
    s = s.lower()
    s = ''.join(ch for ch in s if ch.isalpha())
    n = 116
    palindromes = set()
    for i in range(len(s) - n + 1):
        substr = s[i:i + n]
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes
