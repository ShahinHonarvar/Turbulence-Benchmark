
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(3, 301):
        for j in range(i, len(string)):
            substr = string[j-i+1:j+1]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
