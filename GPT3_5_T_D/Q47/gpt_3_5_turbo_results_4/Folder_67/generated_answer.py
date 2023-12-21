
def palindromes_of_specific_lengths(string):
    substring = string[65:100]
    substring = substring.lower()
    palindromes = set()
    
    for length in range(26, 34):
        for start in range(len(substring) - length + 1):
            end = start + length
            candidate = substring[start:end]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    
    return palindromes
