
def palindromes_between_indices(s):
    english_letters = "abcdefghijklmnopqrstuvwxyz"
    palindromes = set()
    for i in range(2, 5):
        for j in range(i+2, len(s)+1):
            substr = s[i:j]
            if len(substr) >= 3 and all(c in english_letters for c in substr):
                if substr == substr[::-1]:
                    palindromes.add(substr)
    return palindromes
