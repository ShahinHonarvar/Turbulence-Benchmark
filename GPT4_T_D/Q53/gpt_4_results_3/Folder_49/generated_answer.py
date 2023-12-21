
def palindrome_of_length_at_least_n(s):
    s = "".join(char.lower() for char in s if char.isalpha())
    n = 73
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + n - 1, len(s)):
            sub = s[i:j + 1]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes
