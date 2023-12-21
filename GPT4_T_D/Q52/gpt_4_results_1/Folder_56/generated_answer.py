
def palindrome_of_length_n(s):
    s = s.lower()
    l = len(s)
    palindromes = set()
    for i in range(l):
        for j in range(i+95, min(l+1, i+96)):
            substr = s[i:j]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes
