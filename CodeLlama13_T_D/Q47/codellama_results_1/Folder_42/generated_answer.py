
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(43, 96):
        for j in range(i + 18, i + 48):
            if j < len(string) and string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
