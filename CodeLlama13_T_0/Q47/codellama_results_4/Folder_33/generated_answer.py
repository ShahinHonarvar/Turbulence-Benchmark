
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(130, 296):
        for j in range(i+102, i+159):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
