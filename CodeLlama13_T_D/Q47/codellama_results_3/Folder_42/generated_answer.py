
def palindromes_of_specific_lengths(string):
    indices = range(43, 96)
    lengths = range(18, 48)
    palindromes = set()
    for i in indices:
        for j in lengths:
            if string[i:i+j] == string[i+j-1::-1]:
                palindromes.add(string[i:i+j])
    return palindromes
