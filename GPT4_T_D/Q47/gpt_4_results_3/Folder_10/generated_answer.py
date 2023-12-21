
def palindromes_of_specific_lengths(s):
    palindrome_set = set()
    for i in range(16, 61):
        for j in range(i + 16, min(i + 40, 61)):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindrome_set.add(substring.lower())
    return palindrome_set
