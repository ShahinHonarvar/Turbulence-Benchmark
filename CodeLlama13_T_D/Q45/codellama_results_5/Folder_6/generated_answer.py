
def palindromes_between_indices(string):
    palindromes = set()
    for i in range(0, 8):
        for j in range(i+3, 8):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
