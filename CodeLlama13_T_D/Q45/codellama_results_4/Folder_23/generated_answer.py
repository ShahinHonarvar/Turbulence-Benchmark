
def palindromes_between_indices(string):
    palindromes = set()
    for i in range(0, 7):
        for j in range(i + 4, len(string)):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
