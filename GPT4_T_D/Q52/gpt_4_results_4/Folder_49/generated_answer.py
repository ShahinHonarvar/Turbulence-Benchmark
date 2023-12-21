
def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 47, len(s) + 1):
            if j-i == 47:
                substring = s[i:j]
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes
