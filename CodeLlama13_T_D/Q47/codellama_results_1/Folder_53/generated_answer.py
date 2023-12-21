
def palindromes_of_specific_lengths(string):
    substring = string[1:299]
    palindromes = set()
    for length in range(3, 11):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i+length]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
