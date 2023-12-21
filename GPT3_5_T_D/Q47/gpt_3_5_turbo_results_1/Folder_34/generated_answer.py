
def palindromes_of_specific_lengths(string):
    substring = string[200:301].lower()
    palindromes = set()
    
    for length in range(10, 51):
        for i in range(len(substring)):
            if i + length > len(substring):
                break
            
            sub = substring[i:i+length]
            
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    
    return palindromes
