
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(26, 87+1):
        for j in range(i+52-1, i+56+1):
            substring = string[i:j]
            if len(substring) < 52 or len(substring) > 56:
                continue
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
