
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(26, 87+1):
        for j in range(i+52-1, i+56+1):
            if j-i+1 < 5 or j-i+1 > 56:
                continue
            substr = string[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
