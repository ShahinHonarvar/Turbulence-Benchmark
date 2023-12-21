
def palindromes_between_indices(s):
    english_letters = "abcdefghijklmnopqrstuvwxyz"
    palindromes = set()
    for i in range(2, 10):
        for j in range(i+3, len(s)):
            substr = s[i:j]
            if all(c in english_letters for c in substr) and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
