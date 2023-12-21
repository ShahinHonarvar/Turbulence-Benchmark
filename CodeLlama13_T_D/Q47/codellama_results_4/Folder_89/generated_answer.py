
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(12, 15):
        for j in range(i+1, len(string)):
            substr = string[j-i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
