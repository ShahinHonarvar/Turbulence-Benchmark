
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(16, 60 + 1):
        for j in range(i, 39 + 1):
            substring = string[i:j]
            if substring == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes
