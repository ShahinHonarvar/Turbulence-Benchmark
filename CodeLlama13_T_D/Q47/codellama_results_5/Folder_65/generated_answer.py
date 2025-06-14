
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(15, 96):
        for j in range(i+20, i+67):
            substring = string[i:j]
            if len(substring) > 66:
                continue
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
