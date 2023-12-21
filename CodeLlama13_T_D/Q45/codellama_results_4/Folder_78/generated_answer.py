
def palindromes_between_indices(s):
    palindromes = set()
    for i in range(6, 9):
        for j in range(i+2, len(s)):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
