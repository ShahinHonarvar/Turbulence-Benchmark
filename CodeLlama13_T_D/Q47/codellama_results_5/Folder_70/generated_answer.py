
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(10, 70 + 1):
        for j in range(i + 24 - 1, min(i + 52 + 1, len(string))):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
