
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(3, 15 + 1):
        for j in range(0, 100 - i + 1):
            if string[j:j+i] == string[j+i-1::-1]:
                palindromes.add(string[j:j+i])
    return palindromes
