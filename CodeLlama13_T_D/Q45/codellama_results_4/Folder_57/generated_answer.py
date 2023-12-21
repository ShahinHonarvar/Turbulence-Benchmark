
def palindromes_between_indices(string):
    letters = set("abcdefghijklmnopqrstuvwxyz")
    palindromes = set()
    for i in range(2, 6):
        for j in range(i+4, len(string)):
            substring = string[i:j]
            if all(letter in letters for letter in substring) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
