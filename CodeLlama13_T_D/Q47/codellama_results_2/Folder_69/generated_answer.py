
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(11, 97):
        for j in range(i+45-1, i+52):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
