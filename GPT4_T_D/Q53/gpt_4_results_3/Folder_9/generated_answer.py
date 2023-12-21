
def palindrome_of_length_at_least_n(s):
    s = ''.join(ch for ch in s if ch.isalpha()).lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 95, len(s) + 1):
            sub = s[i:j]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes
