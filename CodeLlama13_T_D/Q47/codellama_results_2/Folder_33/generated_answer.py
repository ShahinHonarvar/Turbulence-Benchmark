
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(130, 296):
        for j in range(i+102, i+159):
            substr = string[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
