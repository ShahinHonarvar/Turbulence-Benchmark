
def palindromes_between_indices(string):
    palindromes = set()
    for i in range(3, 10):
        for j in range(i, len(string) - i + 1):
            substring = string[j:j+i]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
