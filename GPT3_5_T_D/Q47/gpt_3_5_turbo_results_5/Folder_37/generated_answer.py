
def palindromes_of_specific_lengths(s):
    s = s[:10].lower()
    palindromes_set = set()
    for i in range(3, 6):
        for j in range(len(s) - i + 1):
            substring = s[j:j + i]
            if substring == substring[::-1] and substring.isalpha():
                palindromes_set.add(substring)
    return palindromes_set
