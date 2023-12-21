
def palindromes_between_indices(string):
    palindromes = set()
    for i in range(1, 8):
        for j in range(i + 6 - 1, len(string)):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
