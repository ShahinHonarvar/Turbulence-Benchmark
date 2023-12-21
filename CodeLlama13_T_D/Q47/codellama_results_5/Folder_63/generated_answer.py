
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(33, 86):
        for j in range(i+25, min(i+31, len(string))):
            if string[i:j] == string[i:j][::-1].lower():
                palindromes.add(string[i:j])
    return palindromes
