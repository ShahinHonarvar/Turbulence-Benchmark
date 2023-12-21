
def palindromes_between_indices(string):
    palindromes = set()
    for i in range(5, 10):
        for j in range(i+1, 11):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
