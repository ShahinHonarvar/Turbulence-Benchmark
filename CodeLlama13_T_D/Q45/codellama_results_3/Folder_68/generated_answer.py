
def palindromes_between_indices(string):
    palindromes = set()
    for i in range(1, 9):
        for j in range(i+3, len(string)+1):
            substr = string[i:j]
            if len(substr) >= 4 and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
