
def palindromes_between_indices(string):
    indices = range(3, 7)
    letters = set("abcdefghijklmnopqrstuvwxyz")
    palindromes = set()
    for i in indices:
        for j in indices:
            if j - i + 1 < 3:
                continue
            substr = string[i:j+1]
            if len(set(substr)) == 2 and all(letter in letters for letter in substr):
                palindromes.add(substr)
    return palindromes
