
def palindromes_between_indices(s):
    letters = "abcdefghijklmnopqrstuvwxyz"
    palindromes = set()
    for i in range(4, 10):
        for j in range(i + 3, len(s)):
            substr = s[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
