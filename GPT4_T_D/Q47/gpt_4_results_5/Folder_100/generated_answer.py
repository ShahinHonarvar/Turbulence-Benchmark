
def palindromes_of_specific_lengths(s):
    s = s[29:97].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 12, i + 19):
            if j > len(s):
                break
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes
