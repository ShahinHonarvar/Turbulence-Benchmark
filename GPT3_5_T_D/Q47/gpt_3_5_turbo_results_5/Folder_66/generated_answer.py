
def palindromes_of_specific_lengths(string):
    substring = string[32:80].lower()
    palindromes = set()
    
    for length in range(35, 42):
        for i in range(len(substring) - length + 1):
            substring_segment = substring[i:i+length]
            if substring_segment.isalpha() and substring_segment == substring_segment[::-1]:
                palindromes.add(substring_segment)
    
    return palindromes
