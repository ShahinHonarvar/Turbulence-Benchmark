
def palindromes_between_indices(s):
    palindromes = set()
    for i in range(2, 6):
        for j in range(i+3, len(s)):
            substr = s[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
