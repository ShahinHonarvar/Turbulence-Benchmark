
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(28, 95):
        for j in range(i+37, i+50):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
