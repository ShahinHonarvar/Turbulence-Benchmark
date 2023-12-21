
def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s.lower()
    for i in range(7):
        for j in range(i+3, min(i+7, 7)):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes
