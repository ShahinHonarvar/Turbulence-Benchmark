
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(44, 100):
        for j in range(i + 13, min(99, i + 42)):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
