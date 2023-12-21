
def palindromes_between_indices(string):
    indices = range(3, 8)
    letters = "abcdefghijklmnopqrstuvwxyz"
    palindromes = set()
    for i in indices:
        for j in range(i+1, len(string)):
            substr = string[i:j]
            if all(letter in letters for letter in substr) and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
