
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(27, 78):
        for j in range(i+18, i+20):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
