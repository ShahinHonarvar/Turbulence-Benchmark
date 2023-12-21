
def palindrome_of_length_n(s):
    s = s.lower()
    length = 63
    palindromes = set()

    for i in range(len(s)):
        for j in range(i + length, min(i + length + 1, len(s) + 1)):
            substr = s[i:j]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)

    return palindromes
