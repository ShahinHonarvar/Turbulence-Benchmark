
def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s)-2):
        for j in range(i+2, len(s)+1):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes
