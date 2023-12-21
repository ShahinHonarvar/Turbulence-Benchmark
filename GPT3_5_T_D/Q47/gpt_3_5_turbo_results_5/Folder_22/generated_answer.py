
def palindromes_of_specific_lengths(string):
    substring = string[100:201]
    palindromes = set()
    
    for length in range(5, 11):
        for i in range(len(substring) - length + 1):
            substring_chunk = substring[i:i+length]
            
            if substring_chunk.lower() == substring_chunk.lower()[::-1] and substring_chunk.isalpha():
                palindromes.add(substring_chunk)
    
    return palindromes
