
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(12, 220 + 1):
        for j in range(len(string) - i + 1):
            substring = string[j:j+i]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
