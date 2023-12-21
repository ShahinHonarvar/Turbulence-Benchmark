
def palindromes_between_indices(string):
    letters = set("abcdefghijklmnopqrstuvwxyz")
    palindromes = set()
    for i in range(3, len(string) - 2):
        for j in range(i + 1, len(string)):
            substr = string[i:j]
            if len(substr) >= 4 and all(letter in letters for letter in substr.lower()):
                palindromes.add(substr)
    return palindromes
