
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(11, 87+1):
        for j in range(i+4-1, i+5):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
