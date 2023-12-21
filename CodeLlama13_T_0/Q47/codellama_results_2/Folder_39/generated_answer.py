
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(31, 92):
        for j in range(i+50, i+54):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
