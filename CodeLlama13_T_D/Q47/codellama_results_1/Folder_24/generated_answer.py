
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(12, 93):
        for j in range(i + 42 - 1, min(77, len(string) - i)):
            substring = string[i:i + j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
