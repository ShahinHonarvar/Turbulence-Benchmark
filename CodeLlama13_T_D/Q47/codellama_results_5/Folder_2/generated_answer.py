
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(10, 60):
        for j in range(i+18, i+37):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
