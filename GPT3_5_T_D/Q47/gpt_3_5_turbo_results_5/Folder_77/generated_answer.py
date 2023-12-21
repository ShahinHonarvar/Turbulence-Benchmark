
def palindromes_of_specific_lengths(string):
    index_range = string[103:277].lower()
    palindromes = set()
    
    for length in range(100, 170):
        for i in range(len(index_range) - length + 1):
            substring = index_range[i:i+length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    
    return palindromes
