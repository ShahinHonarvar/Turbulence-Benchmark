
def palindromes_between_indices(string):
    letters = "abcdefghijklmnopqrstuvwxyz"
    palindromes = set()
    for i in range(3, 8):
        for j in range(i+1, 8):
            substring = string[i:j]
            if len(substring) >= 5 and all(letter in letters for letter in substring):
                palindromes.add(substring)
    return palindromes
