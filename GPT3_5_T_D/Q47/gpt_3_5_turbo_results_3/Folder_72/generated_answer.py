
def palindromes_of_specific_lengths(string):
    substring = string[26:91].lower()
    palindromes = set()
    for length in range(27, 59):
        for i in range(len(substring) - length + 1):
            if substring[i:i + length] == substring[i:i + length][::-1]:
                palindromes.add(substring[i:i + length].upper())
    return palindromes
