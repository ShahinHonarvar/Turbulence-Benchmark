
def palindromes_between_indices(string):
    palindromes = set()
    for i in range(1, len(string) - 4 + 1):
        substring = string[i:i+5]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
