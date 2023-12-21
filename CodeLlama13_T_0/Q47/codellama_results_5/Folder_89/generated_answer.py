
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(18, 89):
        for j in range(i+12, i+15):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
