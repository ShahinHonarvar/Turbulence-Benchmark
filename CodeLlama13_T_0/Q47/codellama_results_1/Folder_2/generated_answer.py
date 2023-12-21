
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(10, 60):
        for j in range(i+18, i+37):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
