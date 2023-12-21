
def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()

    for start in range(len(s)):
        for end in range(start + 37, len(s) + 1):
            substring = s[start:end]
            if substring == substring[::-1]:
                palindromes.add(substring)

    return palindromes
