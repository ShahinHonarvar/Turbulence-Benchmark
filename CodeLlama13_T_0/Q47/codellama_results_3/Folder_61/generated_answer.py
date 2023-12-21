
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(0, 31):
        for j in range(i+20, min(i+31, len(string))):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
