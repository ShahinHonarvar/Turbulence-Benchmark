
def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if j - i == 338:
                substring = s[i:j]
                if substring == substring[::-1] and substring.isalpha():
                    palindromes.add(substring)
    return palindromes
