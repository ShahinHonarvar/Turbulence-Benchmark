
def palindromes_between_indices(string):
    indices = range(4, 10)
    palindromes = set()
    for i in indices:
        for j in range(i + 1, len(string)):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
