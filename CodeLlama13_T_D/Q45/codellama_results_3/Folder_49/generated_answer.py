
def palindromes_between_indices(string):
    letters = "abcdefghijklmnopqrstuvwxyz"
    palindromes = set()
    for i in range(5, 8):
        for j in range(i, len(string)):
            substr = string[i:j]
            if len(substr) < 3:
                continue
            if substr == substr[::-1].lower():
                palindromes.add(substr)
    return palindromes
