
def palindromes_of_specific_lengths(string):
    indices = range(30, 96)
    lengths = range(34, 56)
    palindromes = set()
    for i in indices:
        for j in lengths:
            if string[i:i+j] == string[i+j-1:i-1:-1]:
                palindromes.add(string[i:i+j])
    return palindromes
