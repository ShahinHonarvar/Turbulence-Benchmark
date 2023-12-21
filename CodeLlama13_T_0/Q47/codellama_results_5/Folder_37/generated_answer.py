
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(0, 10):
        for j in range(i + 3, min(i + 6, len(string))):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
