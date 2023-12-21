
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(1, 7):
        for j in range(i+2, min(len(string), i+5)):
            substr = string[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
