
def palindromes_of_specific_lengths(string):
    substring = string[18:87]
    palindromes = set()
    for length in range(38, 60 + 1):
        for i in range(len(substring) - length + 1):
            if substring[i:i+length] == substring[i+length-1::-1]:
                palindromes.add(substring[i:i+length])
    return palindromes
