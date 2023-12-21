
def palindromes_of_specific_lengths(string):
    substring = string[43:96]
    palindromes = set()
    for length in range(18, 48):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i+length]
            if candidate.isalpha() and candidate.lower() == candidate.lower()[::-1]:
                palindromes.add(candidate.lower())
    return palindromes
