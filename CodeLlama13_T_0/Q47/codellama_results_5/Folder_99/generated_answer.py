
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(127, 289):
        for j in range(i+118, i+142):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
