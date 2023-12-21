
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 99
    palindromes = set()

    for i in range(len(s)):
        for j in range(i+n, len(s)+1):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
                
    return palindromes
