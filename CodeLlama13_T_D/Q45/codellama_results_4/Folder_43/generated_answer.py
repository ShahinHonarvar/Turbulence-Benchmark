
def palindromes_between_indices(s):
    english_letters = set("abcdefghijklmnopqrstuvwxyz")
    palindromes = set()
    for i in range(2, 6):
        for j in range(i+3, len(s)+1):
            substr = s[i:j]
            if len(substr) >= 4 and all(c in english_letters for c in substr):
                palindromes.add(substr)
    return palindromes
