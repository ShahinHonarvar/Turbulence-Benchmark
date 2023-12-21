
def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+3, len(s)+1):
            substring = s[i:j]
            if len(substring) == 3:
                if substring == substring[::-1] and substring.isalpha():
                    palindromes.add(substring)
    return palindromes
