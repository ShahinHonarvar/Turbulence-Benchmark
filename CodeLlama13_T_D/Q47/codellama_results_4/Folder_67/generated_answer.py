
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(65, 99+1):
        for j in range(i+26, i+33+1):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
