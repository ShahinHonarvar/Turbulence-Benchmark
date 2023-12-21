
def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    for start in range(len(s)):
        for end in range(start, len(s)):
            substring = s[start:end + 1]
            if len(substring) >= 140 and substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes
