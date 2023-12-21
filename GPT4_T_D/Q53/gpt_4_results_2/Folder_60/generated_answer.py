
def palindrome_of_length_at_least_n(s):
    s = ''.join(ch.lower() for ch in s if ch.isalpha())
    n = 80
    palindromes = set()
    for i in range(n, len(s)+1):
        for j in range(len(s)-i+1):
            if s[j:j+i] == s[j:j+i][::-1]:
                palindromes.add(s[j:j+i])
    return palindromes
