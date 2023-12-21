
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(0, 101):
        for j in range(3, 16):
            substr = string[i:i+j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
