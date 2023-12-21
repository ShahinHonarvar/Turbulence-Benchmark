
def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 100, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return {string for string in palindromes if len(string) == 100 and string.isalpha()}
