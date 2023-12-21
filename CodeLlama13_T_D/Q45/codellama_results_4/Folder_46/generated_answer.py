
def palindromes_between_indices(string):
    indices = range(4, 10)
    letters = set("abcdefghijklmnopqrstuvwxyz")
    palindromes = set()
    for i in indices:
        for j in indices:
            if j < i:
                continue
            substr = string[i:j+1]
            if len(substr) >= 6 and all(letter in letters for letter in substr):
                palindromes.add(substr)
    return palindromes
