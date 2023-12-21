
def palindromes_of_specific_lengths(string):
    substring = string[15:95]
    palindromes = set()
    for length in range(18, 74):
        for i in range(len(substring) - length + 1):
            if substring[i:i+length].isalpha() and substring[i:i+length].lower() == substring[i:i+length].lower()[::-1]:
                palindromes.add(substring[i:i+length])
    return palindromes
