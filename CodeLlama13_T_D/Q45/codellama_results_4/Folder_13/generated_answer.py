
def palindromes_between_indices(string):
    indices = range(3, 9+1)
    letters = set("abcdefghijklmnopqrstuvwxyz")
    palindromes = set()
    for i in indices:
        for j in indices:
            if i <= j:
                substr = string[i:j]
                if len(substr) >= 5 and all(letter in letters for letter in substr):
                    palindromes.add(substr)
    return palindromes
