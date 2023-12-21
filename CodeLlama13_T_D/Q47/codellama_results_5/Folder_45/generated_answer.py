
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(70, 141):
        for j in range(i + 2, min(i + 61, len(string))):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
