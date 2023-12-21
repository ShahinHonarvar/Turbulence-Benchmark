
def palindromes_between_indices(string):
    string = string[4:10].lower()
    palindromes = set()

    if len(string) < 6:
        return palindromes

    for i in range(len(string) - 5):
        for j in range(i + 6, len(string) + 1):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)

    return palindromes
