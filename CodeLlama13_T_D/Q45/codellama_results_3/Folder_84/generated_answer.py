
def palindromes_between_indices(string):
    letters = set("abcdefghijklmnopqrstuvwxyz")
    palindromes = set()
    for i in range(4, 10):
        for j in range(i+2, 10):
            substr = string[i:j]
            if len(substr) >= 3 and all(c in letters for c in substr):
                if substr == substr[::-1]:
                    palindromes.add(substr)
    return palindromes
