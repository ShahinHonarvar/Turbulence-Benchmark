
def palindromes_of_specific_lengths(string):
    substring = string[39:95]
    palindromes = set()
    for length in range(14, 53):
        for i in range(len(substring) - length + 1):
            if substring[i : i + length].lower() == substring[i : i + length][::-1]:
                palindromes.add(substring[i : i + length])
    return palindromes
