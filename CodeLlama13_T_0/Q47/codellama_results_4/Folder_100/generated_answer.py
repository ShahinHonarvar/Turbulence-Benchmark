
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(29, 97):
        for j in range(i+12, min(i+18, len(string))):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
