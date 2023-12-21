
def palindromes_between_indices(string):
    palindromes = set()
    for i in range(4, 7):
        for j in range(i, len(string)):
            substring = string[i:j+1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
