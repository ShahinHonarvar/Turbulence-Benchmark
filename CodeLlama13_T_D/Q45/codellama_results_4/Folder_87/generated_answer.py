
def palindromes_between_indices(string):
    indices = range(3, 9 + 1)
    palindromes = set()
    for i in indices:
        for j in range(i - 2, len(string) - (i - 1)):
            substring = string[j:j + i]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
