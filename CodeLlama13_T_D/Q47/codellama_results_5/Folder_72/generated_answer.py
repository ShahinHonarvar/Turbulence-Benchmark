
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(26, 91):
        for j in range(i+27, min(i+59, len(string))):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
