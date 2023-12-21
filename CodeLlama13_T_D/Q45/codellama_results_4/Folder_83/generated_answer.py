
def palindromes_between_indices(string):
    letters = set("abcdefghijklmnopqrstuvwxyz")
    palindromes = set()
    for i in range(2, 10):
        for j in range(i+6, len(string)):
            substring = string[i:j]
            if all(letter in substring for letter in letters) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
