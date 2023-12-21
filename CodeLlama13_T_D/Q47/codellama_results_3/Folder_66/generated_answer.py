
def palindromes_of_specific_lengths(string):
    indices = range(32, 80)
    lengths = range(35, 42)
    palindromes = set()
    for i in indices:
        for j in lengths:
            if string[i:i+j] == string[i+j-1:i-1:-1]:
                palindromes.add(string[i:i+j])
    return palindromes
