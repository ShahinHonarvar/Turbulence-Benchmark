
def palindromes_of_specific_lengths(string):
    import re
    
    substring = string[100:201].lower()
    palindromes = set()
    
    for length in range(5, 11):
        for i in range(len(substring) - length + 1):
            substring_slice = substring[i:i+length]
            if re.match(r'^[a-zA-Z]+$', substring_slice) and substring_slice == substring_slice[::-1]:
                palindromes.add(substring_slice)
    
    return palindromes
