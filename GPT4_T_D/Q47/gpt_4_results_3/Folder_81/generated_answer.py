
def palindromes_of_specific_lengths(string):
    string = string[12:123]
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 12, i + 221):
            substring = string[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring.lower())
    return palindromes
