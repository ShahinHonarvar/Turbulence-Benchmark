
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(23, 78):
        for j in range(i + 13, min(i + 41, len(string))):
            if string[i:j] == string[i:j][::-1].lower():
                palindromes.add(string[i:j])
    return palindromes
