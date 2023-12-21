
def palindromes_between_indices(string):
    english_letters = "abcdefghijklmnopqrstuvwxyz"
    palindromes = set()
    for i in range(3, 9):
        for j in range(i+1, 9):
            substr = string[i:j]
            if len(substr) < 6:
                continue
            rev_substr = reversed(substr)
            if all(c in english_letters for c in substr) and all(c in english_letters for c in rev_substr):
                palindromes.add(substr)
    return palindromes
