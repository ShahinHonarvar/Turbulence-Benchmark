
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(63, 71):
        for j in range(i+4, i+6):
            substring = string[i:j]
            if substring == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes
