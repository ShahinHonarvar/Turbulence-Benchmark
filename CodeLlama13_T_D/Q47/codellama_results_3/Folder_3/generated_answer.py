
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(27, 95):
        for j in range(49, 51):
            substring = string[i:i+j]
            if substring == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes
