
def palindromes_between_indices(string):
    palindromes = set()
    for i in range(6):
        for j in range(i, 6):
            substring = string[i:j+1]
            if len(substring) >= 3 and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
