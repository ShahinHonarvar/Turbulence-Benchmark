
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(14, 91):
        for j in range(55, 72):
            if string[i:i+j] == string[i+j-1::-1]:
                palindromes.add(string[i:i+j])
    return palindromes
