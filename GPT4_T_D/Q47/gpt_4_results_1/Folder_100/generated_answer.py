
def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[29:97]
    for i in range(len(substring)):
        for j in range(i + 12, min(i + 19, len(substring) + 1)):
            candidate = substring[i:j]
            if candidate == candidate[::-1] and candidate.isalpha() and candidate.lower() == candidate[::-1].lower():
                palindromes.add(candidate.lower())
    return palindromes
