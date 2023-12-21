
def palindromes_between_indices(string):
    letters = "abcdefghijklmnopqrstuvwxyz"
    palindromes = set()
    for i in range(0, 5):
        for j in range(i + 2, 6):
            substring = string[i:j]
            if len(substring) >= 3 and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
