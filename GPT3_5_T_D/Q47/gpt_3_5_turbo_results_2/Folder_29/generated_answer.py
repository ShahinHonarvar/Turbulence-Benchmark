
def palindromes_of_specific_lengths(string):
    substring = string[15:95]
    palindromes = set()
    
    for length in range(18, 74):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start+length]
            
            if candidate.lower() == candidate.lower()[::-1] and candidate.isalpha():
                palindromes.add(candidate)
                
    return palindromes
