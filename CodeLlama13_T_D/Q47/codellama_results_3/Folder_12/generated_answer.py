
def palindromes_of_specific_lengths(string):
    indices = range(62, 89)
    lengths = range(18, 22)
    palindromes = set()
    for i in indices:
        for j in lengths:
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
