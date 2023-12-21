
def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for left in range(len(s)):
        for right in range(left + 1, len(s) + 1):
            substr = s[left:right]
            if len(substr) == 289 and substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes
