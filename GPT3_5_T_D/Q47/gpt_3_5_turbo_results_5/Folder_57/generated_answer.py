
def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[16:95].lower()

    for length in range(39, 53):
        for start in range(len(substring) - length + 1):
            substr = substring[start:start+length]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)

    return palindromes
