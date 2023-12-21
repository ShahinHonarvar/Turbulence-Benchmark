
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(3, 6):
        for j in range(0, len(string) - i + 1):
            substring = string[j:j+i]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
