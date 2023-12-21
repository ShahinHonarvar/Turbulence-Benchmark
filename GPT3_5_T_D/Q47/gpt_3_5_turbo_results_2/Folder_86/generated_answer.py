
def palindromes_of_specific_lengths(string):
    substring = string[30:96].lower()
    palindromes = set()

    for length in range(34, 56):
        for start in range(len(substring) - length + 1):
            substr = substring[start:start + length]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)

    return palindromes
