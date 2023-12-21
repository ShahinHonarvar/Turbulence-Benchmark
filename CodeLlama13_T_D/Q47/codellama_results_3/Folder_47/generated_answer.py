
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(39, 95):
        for j in range(i + 14, i + 53):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
