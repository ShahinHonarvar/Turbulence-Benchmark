
def palindromes_between_indices(string):
    english_letters = set("abcdefghijklmnopqrstuvwxyz")
    palindromes = set()
    for i in range(1, 7):
        for j in range(i + 2, 8):
            substring = string[i:j]
            if len(substring) >= 3 and all(letter in english_letters for letter in substring):
                palindromes.add(substring)
    return palindromes
