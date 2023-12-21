
def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[13:100]
    
    for length in range(26, 30):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i+length]
            candidate_lower = candidate.lower()
            
            if candidate_lower == candidate_lower[::-1] and candidate_lower.isalpha():
                palindromes.add(candidate_lower)
    
    return palindromes
