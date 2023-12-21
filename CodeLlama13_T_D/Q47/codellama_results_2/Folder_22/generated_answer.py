
def palindromes_of_specific_lengths(string):
    substring = string[100:200]
    palindromes = set()
    for i in range(5, 11):
        for j in range(len(substring) - i + 1):
            if substring[j:j+i].lower() == substring[j:j+i][::-1]:
                palindromes.add(substring[j:j+i])
    return palindromes
