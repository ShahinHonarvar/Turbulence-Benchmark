
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(12, 93):
        for j in range(i+17, min(len(string), i+67)):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
