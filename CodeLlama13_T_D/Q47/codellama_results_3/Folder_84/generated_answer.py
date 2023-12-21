
def palindromes_of_specific_lengths(string):
    substring = string[23:78]
    palindromes = set()
    for i in range(13, 41):
        for j in range(len(substring) - i + 1):
            if substring[j:j+i] == substring[j+i-1::-1]:
                palindromes.add(substring[j:j+i])
    return palindromes
