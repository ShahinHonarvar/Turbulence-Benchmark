
def palindromes_between_indices(string):
    palindromes = set()
    for i in range(1, 6):
        for j in range(i + 1, len(string)):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
