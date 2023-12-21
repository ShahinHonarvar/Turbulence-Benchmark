
def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if j - i == 474 and s[i:j] == s[i:j][::-1] and s[i:j].isalpha():
                palindromes.add(s[i:j])
    return palindromes
