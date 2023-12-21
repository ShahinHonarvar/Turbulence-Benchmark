
def palindromes_of_specific_lengths(string):
    substring = string[63:71]
    palindromes = set()
    for i in range(4, 6):
        for j in range(i+1):
            if substring[j:i+j] == substring[i+j:2*i+j][::-1]:
                palindromes.add(substring[j:i+j])
    return palindromes
