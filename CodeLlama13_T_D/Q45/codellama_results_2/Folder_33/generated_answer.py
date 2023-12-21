
def palindromes_between_indices(string):
    letters = set("abcdefghijklmnopqrstuvwxyz")
    palindromes = set()
    for i in range(7, 10):
        for j in range(i + 1, 10):
            substr = string[i:j]
            if len(substr) >= 4 and all(letter in letters for letter in substr.lower()):
                palindromes.add(substr)
    return palindromes
