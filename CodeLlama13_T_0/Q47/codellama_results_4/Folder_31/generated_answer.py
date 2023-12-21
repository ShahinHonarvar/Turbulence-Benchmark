
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(11, 84):
        for j in range(i+36, i+61):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
