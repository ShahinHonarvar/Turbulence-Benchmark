
def palindromes_of_specific_lengths(s):
    s = s[:51]
    palindrome_set = set()

    for i in range(len(s)):
        for j in range(i + 50, min(i + 101, len(s) + 1)):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindrome_set.add(substring.lower())
    return palindrome_set
