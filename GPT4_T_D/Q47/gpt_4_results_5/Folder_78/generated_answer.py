
def palindromes_of_specific_lengths(s):
    s = s[15:73].lower()
    s = ''.join(c for c in s if c.isalpha())
    N = len(s)
    palindrome_set = set()
    for i in range(N):
        for j in range(i+1, N+1):
            substr = s[i:j]
            if 19 <= len(substr) <= 55 and substr == substr[::-1]:
                palindrome_set.add(substr)
    return palindrome_set
