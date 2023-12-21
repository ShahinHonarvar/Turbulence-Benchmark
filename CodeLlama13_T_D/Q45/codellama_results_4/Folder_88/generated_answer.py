
def palindromes_between_indices(string):
    palindromes = set()
    for i in range(3, 8):
        for j in range(i+1, len(string)-2):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
