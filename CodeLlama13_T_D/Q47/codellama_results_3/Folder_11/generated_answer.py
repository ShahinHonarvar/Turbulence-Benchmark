
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(24, 98):
        for j in range(i+10, i+37):
            substring = string[i:j]
            if len(substring) > 1 and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
