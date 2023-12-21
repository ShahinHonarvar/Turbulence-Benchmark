
def palindromes_between_indices(string):
    indices = range(6, 9 + 1)
    letters = set("abcdefghijklmnopqrstuvwxyz")
    palindromes = set()
    for i in indices:
        for j in range(i, len(string)):
            substr = string[i:j]
            if all(letter in letters for letter in substr) and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
