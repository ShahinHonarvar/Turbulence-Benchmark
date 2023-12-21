
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(22, 96):
        for j in range(i + 52 - 1, i + 55):
            if string[i:j].lower() == string[i:j][::-1].lower():
                palindromes.add(string[i:j])
    return palindromes
