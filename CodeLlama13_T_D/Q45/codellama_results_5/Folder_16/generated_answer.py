
def palindromes_between_indices(s):
    indices = range(6, 10)
    letters = set("aebdfhijklmnoqrstuvwxyz")
    palindromes = set()
    for i in indices:
        for j in range(i + 1, len(s)):
            substring = s[i:j]
            if len(substring) < 5:
                continue
            if all(letter in letters for letter in substring):
                palindromes.add(substring)
    return palindromes
