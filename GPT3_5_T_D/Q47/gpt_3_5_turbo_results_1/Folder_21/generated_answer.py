
def palindromes_of_specific_lengths(string):
    string = string[100:296]
    palindromes = set([])
    
    for i in range(len(string)):
        for j in range(136, 161):
            substring = string[i:i+j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring.lower())
                
    return palindromes
