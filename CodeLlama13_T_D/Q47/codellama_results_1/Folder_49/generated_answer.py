
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(10, 100 + 1):
        for j in range(i - 10, i + 1):
            if string[j] == string[j - i]:
                palindromes.add(string[j - i:j])
    return palindromes
