
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(33, 86):
        for j in range(i+25, min(len(string), i+32)):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
