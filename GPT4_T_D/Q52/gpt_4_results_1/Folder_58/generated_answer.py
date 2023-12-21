
def palindrome_of_length_n(s):
    s = s.lower()
    length = 223
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + length, len(s) + 1):
            substring = s[i:j]
            if len(substring) == length and substring == substring[::-1] and substring.replace(" ","").isalpha():
                palindromes.add(substring)
    return palindromes
