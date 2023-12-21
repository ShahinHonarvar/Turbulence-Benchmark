
def palindromes_of_specific_lengths(string):
    substring = string[31:71]
    
    palindromes = set()
    for length in range(21, 33):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.lower() == candidate.lower()[::-1]:
                if candidate.isalpha():
                    palindromes.add(candidate)
    
    return palindromes
