
def palindromes_of_specific_lengths(string):
    substring = string[26:88].lower()
    palindromes = set()
    
    for length in range(52, 57):
        for i in range(len(substring) - length + 1):
            substring_slice = substring[i:i + length]
            if substring_slice.isalpha() and substring_slice == substring_slice[::-1]:
                palindromes.add(substring_slice)
    
    return palindromes
