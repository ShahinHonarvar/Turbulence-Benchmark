
def palindromes_between_indices(string):
    indices = [7, 8, 9]
    letters = set("abcdefghijklmnopqrstuvwxyz")
    palindromes = set()
    for i in range(len(string) - 3):
        substr = string[i:i+4]
        if len(substr) < 4 or not all(c in letters for c in substr):
            continue
        for j in indices:
            palindromes.add("".join(substr[:j-i] + substr[j-i:][::-1]))
    return palindromes
