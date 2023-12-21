
def palindromes_between_indices(s):
    english_letters = "abcdefghijklmnopqrstuvwxyz"
    palindromes = set()
    for i in range(6, 9):
        for j in range(i+3, len(s)):
            substr = s[i:j]
            if len(substr) >= 4 and all(c in english_letters for c in substr):
                if substr == substr[::-1]:
                    palindromes.add(substr)
    return palindromes
