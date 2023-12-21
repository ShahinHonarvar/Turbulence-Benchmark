
def palindromes_of_specific_lengths(string):
    substring = string[23:95]
    palindromes = set()
    
    for length in range(17, 56):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length].lower()
            if candidate.isalpha() and candidate == candidate[::-1]:
                palindromes.add(candidate)
    
    return palindromes
