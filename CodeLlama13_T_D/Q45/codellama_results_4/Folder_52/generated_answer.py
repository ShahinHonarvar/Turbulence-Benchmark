
def palindromes_between_indices(string):
    letters = set("abcdefghijklmnopqrstuvwxyz")
    indices = range(0, 8)
    palindromes = []
    for i in indices:
        for j in range(i + 1, 8):
            substring = string[i:j]
            if len(substring) >= 6 and all(letter in letters for letter in substring.lower()):
                palindromes.append("".join(reversed(substring)))
    return set(palindromes)
