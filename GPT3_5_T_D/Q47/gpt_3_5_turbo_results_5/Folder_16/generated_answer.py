
def palindromes_of_specific_lengths(string):
    index_range = slice(15, 87)
    substring = string[index_range].lower()
    
    palindromes = set()
    for length in range(51, 61):
        for i in range(len(substring) - length + 1):
            if substring[i:i+length].isalpha() and substring[i:i+length] == substring[i:i+length][::-1]:
                palindromes.add(substring[i:i+length])

    return palindromes
