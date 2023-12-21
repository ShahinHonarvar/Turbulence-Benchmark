
def palindromes_of_specific_lengths(string):
    substring = string[33:86].lower()
    palindromes = set()
    
    for length in range(26, 32):
        for i in range(len(substring)-length+1):
            substring_slice = substring[i:i+length]
            if substring_slice == substring_slice[::-1] and substring_slice.isalpha():
                palindromes.add(substring_slice)

    return palindromes
