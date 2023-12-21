
def palindromes_of_specific_lengths(s):
    s = s[23:83]
    palindrome_set = set()
    for length in range(32, 35):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.lower() == substring.lower()[::-1] and substring.isalpha():
                palindrome_set.add(substring)
    return palindrome_set
