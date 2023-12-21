
def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substr = s[i:j]
            if len(substr) == 72 and substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes
