
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 32, len(s) + 1):
            sub = s[i:j]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes
